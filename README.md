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