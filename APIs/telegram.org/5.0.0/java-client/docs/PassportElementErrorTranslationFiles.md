

# PassportElementErrorTranslationFiles

Represents an issue with the translated version of a document. The error is considered resolved when a file with the document translation change.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**fileHashes** | **List&lt;String&gt;** | List of base64-encoded file hashes |  |
|**message** | **String** | Error message |  |
|**source** | **String** | Error source, must be *translation\\_files* |  |
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



