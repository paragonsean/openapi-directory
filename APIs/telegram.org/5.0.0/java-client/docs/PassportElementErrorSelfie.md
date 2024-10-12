

# PassportElementErrorSelfie

Represents an issue with the selfie with a document. The error is considered resolved when the file with the selfie changes.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**fileHash** | **String** | Base64-encoded hash of the file with the selfie |  |
|**message** | **String** | Error message |  |
|**source** | **String** | Error source, must be *selfie* |  |
|**type** | [**TypeEnum**](#TypeEnum) | The section of the user&#39;s Telegram Passport which has the issue, one of “passport”, “driver\\_license”, “identity\\_card”, “internal\\_passport” |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| PASSPORT | &quot;passport&quot; |
| DRIVER_LICENSE | &quot;driver_license&quot; |
| IDENTITY_CARD | &quot;identity_card&quot; |
| INTERNAL_PASSPORT | &quot;internal_passport&quot; |



