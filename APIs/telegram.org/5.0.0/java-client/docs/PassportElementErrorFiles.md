

# PassportElementErrorFiles

Represents an issue with a list of scans. The error is considered resolved when the list of files containing the scans changes.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**fileHashes** | **List&lt;String&gt;** | List of base64-encoded file hashes |  |
|**message** | **String** | Error message |  |
|**source** | **String** | Error source, must be *files* |  |
|**type** | [**TypeEnum**](#TypeEnum) | The section of the user&#39;s Telegram Passport which has the issue, one of “utility\\_bill”, “bank\\_statement”, “rental\\_agreement”, “passport\\_registration”, “temporary\\_registration” |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| UTILITY_BILL | &quot;utility_bill&quot; |
| BANK_STATEMENT | &quot;bank_statement&quot; |
| RENTAL_AGREEMENT | &quot;rental_agreement&quot; |
| PASSPORT_REGISTRATION | &quot;passport_registration&quot; |
| TEMPORARY_REGISTRATION | &quot;temporary_registration&quot; |



