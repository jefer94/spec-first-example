# Payment Spec

## Feature: Process payments

### Scenario: Successful payment
- Given a valid payment amount greater than zero
- And a valid card token
- When `process_payment(amount, card_token)` is called
- Then it returns a transaction ID

### Scenario: Rejected payment with zero amount
- Given an amount of zero
- When `process_payment(amount, card_token)` is called
- Then it raises `InvalidAmountError`

### Scenario: Rejected payment with negative amount
- Given a negative amount
- When `process_payment(amount, card_token)` is called
- Then it raises `InvalidAmountError`
