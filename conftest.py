import time
import pytest

BASE_URL = "https://sv-students-recommend.onrender.com"


@pytest.fixture
def api(playwright):
    request_context = playwright.request.new_context(
        base_url=BASE_URL
    )

    yield request_context

    request_context.dispose()


def unique_user():
    stamp = int(time.time() * 1000)

    return {
        "name": f"User_{stamp}",
        "email": f"user_{stamp}@gmail.com",
        "password": f"Pass{stamp}"
    }


def register_user(api):
    user = unique_user()

    response = api.post(
        "/auth/register",
        data={
            "name": user["name"],
            "email": user["email"],
            "password": user["password"]
        }
    )

    assert response.status in [200, 201], response.text()

    return user


def login_user(api, email, password):
    response = api.post(
        "/auth/login",
        data={
            "email": email,
            "password": password
        }
    )

    return response


def get_token(api, email, password):
    response = login_user(api, email, password)

    assert response.status == 200, response.text()

    body = response.json()

    token = body.get("access_token") or body.get("token")

    assert token is not None, body

    return token


def auth_headers(token):
    return {
        "Authorization": f"Bearer {token}"
    }

@pytest.fixture
def test_user(api):
    user = register_user(api)
    print(f"\nCreated: {user['email']}")

    yield user

    print(f"\n[Cleanup] Starting automatic deletion for: {user['email']} 🧹")
    try:
        token = get_token(
            api,
            user["email"],
            user["password"]
        )

        headers = auth_headers(token)

        response = api.delete(
            f"/api/profile/me",
            headers=headers
        )

        assert response.status in [200, 204]
        print(f"[Cleanup] User {user['email']} successfully deleted! 🟢")
    except Exception as e:
        print(f"[Cleanup] Error deleting user: {e} 🔴")

