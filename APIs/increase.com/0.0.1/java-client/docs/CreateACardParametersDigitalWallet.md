

# CreateACardParametersDigitalWallet

The contact information used in the two-factor steps for digital wallet card creation. To add the card to a digital wallet, you may supply an email or phone number with this request. Otherwise, subscribe and then action a Real Time Decision with the category `digital_wallet_token_requested` or `digital_wallet_authentication_requested`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cardProfileId** | **String** | The card profile assigned to this digital card. Card profiles may also be assigned at the program level. |  [optional] |
|**email** | **String** | An email address that can be used to verify the cardholder via one-time passcode over email. |  [optional] |
|**phone** | **String** | A phone number that can be used to verify the cardholder via one-time passcode over SMS. |  [optional] |



