

# PassportElementErrorFile

Represents an issue with a document scan. The error is considered resolved when the file with the document scan changes.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**fileHash** | **String** | Base64-encoded file hash |  |
|**message** | **String** | Error message |  |
|**source** | **String** | Error source, must be *file* |  |
|**type** | [**TypeEnum**](#TypeEnum) | The section of the user&#39;s Telegram Passport which has the issue, one of “utility\\_bill”, “bank\\_statement”, “rental\\_agreement”, “passport\\_registration”, “temporary\\_registration” |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| UTILITY_BILL | &quot;utility_bill&quot; |
| BANK_STATEMENT | &quot;bank_statement&quot; |
| RENTAL_AGREEMENT | &quot;rental_agreement&quot; |
| PASSPORT_REGISTRATION | &quot;passport_registration&quot; |
| TEMPORARY_REGISTRATION | &quot;temporary_registration&quot; |



