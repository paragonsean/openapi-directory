

# PassportElementErrorReverseSide

Represents an issue with the reverse side of a document. The error is considered resolved when the file with reverse side of the document changes.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**fileHash** | **String** | Base64-encoded hash of the file with the reverse side of the document |  |
|**message** | **String** | Error message |  |
|**source** | **String** | Error source, must be *reverse\\_side* |  |
|**type** | [**TypeEnum**](#TypeEnum) | The section of the user&#39;s Telegram Passport which has the issue, one of “driver\\_license”, “identity\\_card” |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| DRIVER_LICENSE | &quot;driver_license&quot; |
| IDENTITY_CARD | &quot;identity_card&quot; |



