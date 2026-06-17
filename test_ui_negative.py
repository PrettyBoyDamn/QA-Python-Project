from playwright.sync_api import Page, expect
from conftest import register_user, get_token, auth_headers
import time

BASE_URL = "https://sv-students-recommend.onrender.com"

ADMIN_EMAIL = "hagai@svcollege.co.il"
ADMIN_PASSWORD = "test1234"


def login_admin_ui(page: Page):
    page.goto(f"{BASE_URL}/pages/login.html")

    page.locator("[data-test='input-email']").fill(ADMIN_EMAIL)
    page.locator("[data-test='input-password']").fill(ADMIN_PASSWORD)
    page.locator("[data-test='btn-login']").click()

    expect(page).to_have_url(f"{BASE_URL}/pages/home.html")


def block_email_as_admin(page: Page, email: str):
    login_admin_ui(page)

    page.locator("[data-test='nav-system']").click()
    page.locator("[data-test='input-blacklist-email']").fill(email)
    page.locator("[data-test='btn-add-blacklist']").click()


def login_user_ui(page: Page, user):
    page.goto(f"{BASE_URL}/pages/login.html")

    page.locator("[data-test='input-email']").fill(user["email"])
    page.locator("[data-test='input-password']").fill(user["password"])
    page.locator("[data-test='btn-login']").click()

    expect(page).to_have_url(f"{BASE_URL}/pages/home.html")


def test_u12_access_control_via_url(page: Page, test_user):
    login_user_ui(page, test_user)

    page.goto(f"{BASE_URL}/pages/admin.html")

    expect(page).not_to_have_url(f"{BASE_URL}/pages/admin.html")

def test_u13_banned_user_cannot_log_in(page: Page, test_user):
    block_email_as_admin(page, test_user["email"])

    page.context.clear_cookies()
    page.evaluate("localStorage.clear()")

    page.goto(f"{BASE_URL}/pages/login.html")

    page.locator("[data-test='input-email']").fill(test_user["email"])
    page.locator("[data-test='input-password']").fill(test_user["password"])
    page.locator("[data-test='btn-login']").click()

    expect(page).to_have_url(f"{BASE_URL}/pages/login.html")

def test_u14_blacklisted_email_cannot_register(browser):
    email = "blocked_test_123@gmail.com"

    admin_context = browser.new_context()
    admin_page = admin_context.new_page()

    block_email_as_admin(admin_page, email)

    admin_context.close()

    user_context = browser.new_context()
    page = user_context.new_page()

    page.goto(f"{BASE_URL}/pages/register.html")

    page.locator("[data-test='input-name']").fill("Blocked User")
    page.locator("[data-test='input-email']").fill(email)
    page.locator("[data-test='input-password']").fill("Pass123456")
    page.locator("[data-test='btn-register']").click()

    expect(page).to_have_url(
        f"{BASE_URL}/pages/register.html"
    )

    user_context.close()

def test_u15_payment_empty_full_name(page: Page, test_user):
    login_user_ui(page, test_user)

    page.locator("[data-test='nav-store']").click()
    page.locator("[data-test='btn-add-tshirt']").click()

    page.goto(f"{BASE_URL}/pages/payment.html")

    page.locator("[data-test='input-address']").fill("Herzl 10")
    page.locator("[data-test='input-card-number']").fill("4111111111111111")
    page.locator("[data-test='input-cvv']").fill("123")
    page.locator("[data-test='input-expiry']").fill("2030-12")

    page.locator("[data-test='btn-place-order']").click()

    expect(page).not_to_have_url(
        f"{BASE_URL}/pages/order-confirmation.html"
    )

def test_u16_cannot_edit_someone_elses_recommendation(page: Page, api):
    owner = register_user(api)
    viewer = register_user(api)

    owner_token = get_token(
        api,
        owner["email"],
        owner["password"]
    )

    rec_name = f"Owner Private Recommendation {int(time.time())}"

    create_response = api.post(
        "/api/recommendations",
        headers=auth_headers(owner_token),
        form={
            "category": "Movie",
            "name": rec_name,
            "recommender_name": owner["name"]
        }
    )

    assert create_response.status in [200, 201], create_response.text()

    login_user_ui(page, viewer)

    page.get_by_text(rec_name).click()

    expect(
        page.locator("[data-test='btn-edit-recommendation']")
    ).to_be_hidden()

    expect(
        page.locator("[data-test='btn-delete-recommendation']")
    ).to_be_hidden()