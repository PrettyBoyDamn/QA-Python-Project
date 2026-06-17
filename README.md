## Test Coverage

### API Tests
| Test ID | Test Name | File |
|---|---|---|
| A2 | Login success returns access token | test_api.py |
| A4 | Create recommendation with empty category | test_api.py |
| A5 | Admin can delete existing recommendation | test_api.py |
| A6 | Regular user cannot delete another user’s recommendation | test_api.py |
| A8 | Login with wrong password | test_api.py |
| A10 | Create recommendation without token | test_api.py |

### Positive UI Tests
| Test ID | Test Name | File |
|---|---|---|
| U4 | Logo navigation | test_ui_positive.py |
| U5 | Register then login | test_ui_positive.py |
| U6 | Filter recommendations | test_ui_positive.py |
| U7 | Add to cart updates counter | test_ui_positive.py |
| U8 | Logout | test_ui_positive.py |

### Negative UI Tests
| Test ID | Test Name | File |
|---|---|---|
| U12 | Access control via URL | test_ui_negative.py |
| U13 | Banned user cannot log in | test_ui_negative.py |
| U14 | Blacklisted email cannot register | test_ui_negative.py |
| U15 | Payment empty full name | test_ui_negative.py |
| U16 | Cannot edit someone else’s recommendation | test_ui_negative.py |

### Boundary UI Tests
| Test ID | Test Name | File |
|---|---|---|
| U17 | Password min valid, 4 chars | test_ui_boundary.py |
| U18 | Password min invalid, 3 chars | test_ui_boundary.py |
| U19 | Cart quantity 0 | test_ui_boundary.py |
| U20 | Empty cart checkout | test_ui_boundary.py |


# All Recent Test Results

## API Tests

| Test ID | Test Name | Expected Result | Status | Actual Result |
|----------|------------|-----------------|---------|----------------|
| A2 | Login success returns access token | User logs in successfully and an access token is returned in the response. | Passed | - |
| A4 | Create recommendation with empty category | System rejects recommendation creation and displays a validation error for the empty category field. | Passed | - |
| A5 | Admin can delete existing recommendation | Admin successfully deletes the selected recommendation and receives a success response. | Passed | - |
| A6 | Regular user cannot delete another user's recommendation | System denies the delete request and returns an authorization error. | Passed | - |
| A8 | Login with wrong password | Login attempt is rejected and an authentication error is returned. | Passed | - |
| A10 | Create recommendation without token | System rejects the request and returns an unauthorized response due to the missing token. | Passed | - |

## Positive UI Tests

| Test ID | Test Name | Expected Result | Status | Actual Result |
|----------|------------|-----------------|---------|----------------|
| U4 | Logo navigation | Clicking the logo redirects the user to the home page. | Passed | - |
| U5 | Register then login | User successfully registers and can log in using the newly created account. | Passed | - |
| U6 | Filter recommendations | Recommendations are filtered according to the selected criteria and only matching recommendations are displayed. | Passed | - |
| U7 | Add to cart updates counter | Adding an item to the cart increases the cart counter by one and updates the cart display. | Failed | nav-cart element is missing. |
| U8 | Logout | User is logged out successfully and redirected to the login page or public page. | Passed | - |

## Negative UI Tests

| Test ID | Test Name | Expected Result | Status | Actual Result |
|----------|------------|-----------------|---------|----------------|
| U12 | Access control via URL | Unauthorized users are denied access and redirected to an appropriate page. | Passed | - |
| U13 | Banned user cannot log in | System prevents the banned user from logging in and displays an error message. | Passed | - |
| U14 | Blacklisted email cannot register | Registration is blocked and an error message is displayed for the blacklisted email. | Passed | - |
| U15 | Payment empty full name | Payment submission is rejected and a validation message is displayed for the empty full name field. | Passed | - |
| U16 | Cannot edit someone else's recommendation | User is denied permission to edit another user's recommendation. | Passed | - |

## Boundary UI Tests

| Test ID | Test Name | Expected Result | Status | Actual Result |
|----------|------------|-----------------|---------|----------------|
| U17 | Password min valid, 4 chars | User is successfully registered and redirected to pages/login.html. | Failed | User was not redirected to pages/login.html. |
| U18 | Password min invalid, 3 chars | System rejects the password and displays a validation error indicating that the minimum length requirement is not met. | Passed | - |
| U19 | Cart quantity 0 | System prevents checkout or correctly handles an item quantity of zero in the cart. | Passed | - |
| U20 | Empty cart checkout | Checkout process is blocked and an appropriate message indicates that the cart is empty. | Passed | - |