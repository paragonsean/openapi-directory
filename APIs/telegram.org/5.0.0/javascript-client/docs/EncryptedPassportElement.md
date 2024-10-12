# TelegramBotApi.EncryptedPassportElement

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **String** | *Optional*. Base64-encoded encrypted Telegram Passport element data provided by the user, available for “personal\\_details”, “passport”, “driver\\_license”, “identity\\_card”, “internal\\_passport” and “address” types. Can be decrypted and verified using the accompanying [EncryptedCredentials](https://core.telegram.org/bots/api/#encryptedcredentials). | [optional] 
**email** | **String** | *Optional*. User&#39;s verified email address, available only for “email” type | [optional] 
**files** | [**[PassportFile]**](PassportFile.md) | *Optional*. Array of encrypted files with documents provided by the user, available for “utility\\_bill”, “bank\\_statement”, “rental\\_agreement”, “passport\\_registration” and “temporary\\_registration” types. Files can be decrypted and verified using the accompanying [EncryptedCredentials](https://core.telegram.org/bots/api/#encryptedcredentials). | [optional] 
**frontSide** | [**PassportFile**](PassportFile.md) |  | [optional] 
**hash** | **String** | Base64-encoded element hash for using in [PassportElementErrorUnspecified](https://core.telegram.org/bots/api/#passportelementerrorunspecified) | 
**phoneNumber** | **String** | *Optional*. User&#39;s verified phone number, available only for “phone\\_number” type | [optional] 
**reverseSide** | [**PassportFile**](PassportFile.md) |  | [optional] 
**selfie** | [**PassportFile**](PassportFile.md) |  | [optional] 
**translation** | [**[PassportFile]**](PassportFile.md) | *Optional*. Array of encrypted files with translated versions of documents provided by the user. Available if requested for “passport”, “driver\\_license”, “identity\\_card”, “internal\\_passport”, “utility\\_bill”, “bank\\_statement”, “rental\\_agreement”, “passport\\_registration” and “temporary\\_registration” types. Files can be decrypted and verified using the accompanying [EncryptedCredentials](https://core.telegram.org/bots/api/#encryptedcredentials). | [optional] 
**type** | **String** | Element type. One of “personal\\_details”, “passport”, “driver\\_license”, “identity\\_card”, “internal\\_passport”, “address”, “utility\\_bill”, “bank\\_statement”, “rental\\_agreement”, “passport\\_registration”, “temporary\\_registration”, “phone\\_number”, “email”. | 



## Enum: TypeEnum


* `personal_details` (value: `"personal_details"`)

* `passport` (value: `"passport"`)

* `driver_license` (value: `"driver_license"`)

* `identity_card` (value: `"identity_card"`)

* `internal_passport` (value: `"internal_passport"`)

* `address` (value: `"address"`)

* `utility_bill` (value: `"utility_bill"`)

* `bank_statement` (value: `"bank_statement"`)

* `rental_agreement` (value: `"rental_agreement"`)

* `passport_registration` (value: `"passport_registration"`)

* `temporary_registration` (value: `"temporary_registration"`)

* `phone_number` (value: `"phone_number"`)

* `email` (value: `"email"`)




