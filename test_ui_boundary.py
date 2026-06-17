from playwright.sync_api import Page, expect
from conftest import register_user, get_token, auth_headers
from test_ui_positive import login_user_ui
import time


BASE_URL = "https://sv-students-recommend.onrender.com"

def test_u17_password_min_valid(page: Page):
    user = {
        "name": "Boundary User",
        "email": f"boundary4_{int(time.time())}@gmail.com",
        "password": "abcd"
    }

    page.goto(f"{BASE_URL}/pages/register.html")

    page.locator("[data-test='input-name']").fill(user["name"])
    page.locator("[data-test='input-email']").fill(user["email"])
    page.locator("[data-test='input-password']").fill(user["password"])

    page.locator("[data-test='btn-register']").click()

    expect(page).to_have_url(
        f"{BASE_URL}/pages/login.html"
    )

def test_u18_password_min_invalid(page: Page):
    page.goto(f"{BASE_URL}/pages/register.html")

    page.locator("[data-test='input-name']").fill("Boundary User")
    page.locator("[data-test='input-email']").fill(
        f"boundary3_{int(time.time())}@gmail.com"
    )
    page.locator("[data-test='input-password']").fill("abc")

    page.locator("[data-test='btn-register']").click()

    expect(page).to_have_url(
        f"{BASE_URL}/pages/register.html"
    )

def test_u19_cart_quantity_zero(page: Page, test_user):
    login_user_ui(page, test_user)

    page.locator("[data-test='nav-store']").click()
    page.locator("[data-test='btn-add-tshirt']").click()

    page.goto(f"{BASE_URL}/pages/cart.html")

    minus_btn = page.locator(
        "[data-test='btn-decrease-tshirt']"
    )

    if minus_btn.count() > 0:
        minus_btn.click()

    assert "Your cart is empty" in page.content() \
        or "0" in page.content()

def test_u20_empty_cart_checkout(page: Page, test_user):
    login_user_ui(page, test_user)

    expect(page).to_have_url(f"{BASE_URL}/pages/home.html")

    page.locator("[data-test='nav-store']").click()

    page.goto(f"{BASE_URL}/pages/cart.html")

    assert "Your cart is empty" in page.content()

    expect(
        page.locator("[data-test='btn-proceed-payment']")
    ).to_be_hidden()