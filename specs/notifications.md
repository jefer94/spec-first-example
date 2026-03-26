# Notifications Spec

## Feature: Send notifications

### Scenario: Successful email notification
- Given a valid recipient email and message
- When `send_notification(email, message)` is called
- Then it returns True

### Scenario: Failed notification with empty email
- Given an empty email string
- When `send_notification(email, message)` is called
- Then it raises `InvalidRecipientError`

### Scenario: Failed notification with empty message
- Given a valid email but empty message
- When `send_notification(email, message)` is called
- Then it raises `InvalidMessageError`
