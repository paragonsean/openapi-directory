

# EncryptedPassportElement

Contains information about documents or other Telegram Passport elements shared with the bot by the user.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**data** | **String** | *Optional*. Base64-encoded encrypted Telegram Passport element data provided by the user, available for “personal\\_details”, “passport”, “driver\\_license”, “identity\\_card”, “internal\\_passport” and “address” types. Can be decrypted and verified using the accompanying [EncryptedCredentials](https://core.telegram.org/bots/api/#encryptedcredentials). |  [optional] |
|**email** | **String** | *Optional*. User&#39;s verified email address, available only for “email” type |  [optional] |
|**files** | [**List&lt;PassportFile&gt;**](PassportFile.md) | *Optional*. Array of encrypted files with documents provided by the user, available for “utility\\_bill”, “bank\\_statement”, “rental\\_agreement”, “passport\\_registration” and “temporary\\_registration” types. Files can be decrypted and verified using the accompanying [EncryptedCredentials](https://core.telegram.org/bots/api/#encryptedcredentials). |  [optional] |
|**frontSide** | [**PassportFile**](PassportFile.md) |  |  [optional] |
|**hash** | **String** | Base64-encoded element hash for using in [PassportElementErrorUnspecified](https://core.telegram.org/bots/api/#passportelementerrorunspecified) |  |
|**phoneNumber** | **String** | *Optional*. User&#39;s verified phone number, available only for “phone\\_number” type |  [optional] |
|**reverseSide** | [**PassportFile**](PassportFile.md) |  |  [optional] |
|**selfie** | [**PassportFile**](PassportFile.md) |  |  [optional] |
|**translation** | [**List&lt;PassportFile&gt;**](PassportFile.md) | *Optional*. Array of encrypted files with translated versions of documents provided by the user. Available if requested for “passport”, “driver\\_license”, “identity\\_card”, “internal\\_passport”, “utility\\_bill”, “bank\\_statement”, “rental\\_agreement”, “passport\\_registration” and “temporary\\_registration” types. Files can be decrypted and verified using the accompanying [EncryptedCredentials](https://core.telegram.org/bots/api/#encryptedcredentials). |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Element type. One of “personal\\_details”, “passport”, “driver\\_license”, “identity\\_card”, “internal\\_passport”, “address”, “utility\\_bill”, “bank\\_statement”, “rental\\_agreement”, “passport\\_registration”, “temporary\\_registration”, “phone\\_number”, “email”. |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| PERSONAL_DETAILS | &quot;personal_details&quot; |
| PASSPORT | &quot;passport&quot; |
| DRIVER_LICENSE | &quot;driver_license&quot; |
| IDENTITY_CARD | &quot;identity_card&quot; |
| INTERNAL_PASSPORT | &quot;internal_passport&quot; |
| ADDRESS | &quot;address&quot; |
| UTILITY_BILL | &quot;utility_bill&quot; |
| BANK_STATEMENT | &quot;bank_statement&quot; |
| RENTAL_AGREEMENT | &quot;rental_agreement&quot; |
| PASSPORT_REGISTRATION | &quot;passport_registration&quot; |
| TEMPORARY_REGISTRATION | &quot;temporary_registration&quot; |
| PHONE_NUMBER | &quot;phone_number&quot; |
| EMAIL | &quot;email&quot; |



