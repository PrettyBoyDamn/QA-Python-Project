import re
from playwright.sync_api import Page, expect
from conftest import unique_user

BASE_URL = "https://sv-students-recommend.onrender.com"


def register_new_user(page: Page):
    user = unique_user()

    page.goto(f"{BASE_URL}/pages/register.html")

    page.locator("[data-test='input-name']").fill(user["name"])
    page.locator("[data-test='input-email']").fill(user["email"])
    page.locator("[data-test='input-password']").fill(user["password"])

    page.locator("[data-test='btn-register']").click()

    return user


def login_user_ui(page: Page, user):
    page.goto(f"{BASE_URL}/pages/login.html")

    page.locator("[data-test='input-email']").fill(
        user["email"]
    )

    page.locator("[data-test='input-password']").fill(
        user["password"]
    )

    page.locator("[data-test='btn-login']").click()

    expect(page).to_have_url(
        f"{BASE_URL}/pages/home.html"
    )

def test_u4_logo_navigation(page: Page, test_user):
    login_user_ui(page, test_user)

    page.goto(f"{BASE_URL}/pages/store.html")

    expect(page).to_have_url(
        f"{BASE_URL}/pages/store.html"
    )

    page.get_by_role(
        "link",
        name="SV College SV Recommend"
    ).click()

    expect(page).to_have_url(
        f"{BASE_URL}/pages/home.html"
    )


def test_u5_register_then_login(page: Page, test_user):
    login_user_ui(page, test_user)

    expect(page).to_have_url(
        f"{BASE_URL}/pages/home.html"
    )

def test_u7_add_to_cart_updates_counter(page: Page, test_user):
    login_user_ui(page, test_user)

    page.locator("[data-test='nav-store']").click()

    page.locator("[data-test='btn-add-tshirt']").click()

    page.wait_for_timeout(500)

    page.locator("[data-test='nav-cart']").click()

    expect(
        page.locator("[data-test='cart-qty-tshirt']")
    ).to_have_text("1")

def test_u6_filter_recommendations(page: Page, test_user):
    login_user_ui(page, test_user)

    page.locator("[data-test='filter-movie']").click()

    page.locator("[data-test='card-category']").first.click()

    expect(
        page.locator("[data-test='detail-category']")
    ).to_have_text("Movie")

def test_u8_logout(page: Page, test_user):
    login_user_ui(page, test_user)

    page.locator("[data-test='nav-logout']").click()

    expect(page).to_have_url(
        f"{BASE_URL}/pages/login.html"
    )