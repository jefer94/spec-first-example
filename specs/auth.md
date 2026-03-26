# Authentication Spec

## Feature: User login

### Scenario: Successful login with valid credentials
- Given a registered user with username and password
- When `login(username, password)` is called with correct credentials
- Then it returns a session token

### Scenario: Failed login with invalid password
- Given a registered user with username and password
- When `login(username, password)` is called with wrong password
- Then it raises `InvalidCredentialsError`

### Scenario: Failed login with unknown username
- Given no user registered with a username
- When `login(username, password)` is called
- Then it raises `InvalidCredentialsError`
