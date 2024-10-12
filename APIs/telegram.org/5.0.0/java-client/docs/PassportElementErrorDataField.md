

# PassportElementErrorDataField

Represents an issue in one of the data fields that was provided by the user. The error is considered resolved when the field's value changes.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataHash** | **String** | Base64-encoded data hash |  |
|**fieldName** | **String** | Name of the data field which has the error |  |
|**message** | **String** | Error message |  |
|**source** | **String** | Error source, must be *data* |  |
|**type** | [**TypeEnum**](#TypeEnum) | The section of the user&#39;s Telegram Passport which has the error, one of “personal\\_details”, “passport”, “driver\\_license”, “identity\\_card”, “internal\\_passport”, “address” |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| PERSONAL_DETAILS | &quot;personal_details&quot; |
| PASSPORT | &quot;passport&quot; |
| DRIVER_LICENSE | &quot;driver_license&quot; |
| IDENTITY_CARD | &quot;identity_card&quot; |
| INTERNAL_PASSPORT | &quot;internal_passport&quot; |
| ADDRESS | &quot;address&quot; |



