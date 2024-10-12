

# PassportElementErrorTranslationFile

Represents an issue with one of the files that constitute the translation of a document. The error is considered resolved when the file changes.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**fileHash** | **String** | Base64-encoded file hash |  |
|**message** | **String** | Error message |  |
|**source** | **String** | Error source, must be *translation\\_file* |  |
|**type** | [**TypeEnum**](#TypeEnum) | Type of element of the user&#39;s Telegram Passport which has the issue, one of “passport”, “driver\\_license”, “identity\\_card”, “internal\\_passport”, “utility\\_bill”, “bank\\_statement”, “rental\\_agreement”, “passport\\_registration”, “temporary\\_registration” |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| PASSPORT | &quot;passport&quot; |
| DRIVER_LICENSE | &quot;driver_license&quot; |
| IDENTITY_CARD | &quot;identity_card&quot; |
| INTERNAL_PASSPORT | &quot;internal_passport&quot; |
| UTILITY_BILL | &quot;utility_bill&quot; |
| BANK_STATEMENT | &quot;bank_statement&quot; |
| RENTAL_AGREEMENT | &quot;rental_agreement&quot; |
| PASSPORT_REGISTRATION | &quot;passport_registration&quot; |
| TEMPORARY_REGISTRATION | &quot;temporary_registration&quot; |



