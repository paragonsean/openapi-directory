

# PerDeviceStatusInBatch

Captures the processing status for each device in the operation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**deviceId** | **String** | If processing succeeds, the device ID of the device. |  [optional] |
|**errorIdentifier** | **String** | If processing fails, the error type. |  [optional] |
|**errorMessage** | **String** | If processing fails, a developer message explaining what went wrong. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The result status of the device after processing. |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;SINGLE_DEVICE_STATUS_UNSPECIFIED&quot; |
| UNKNOWN_ERROR | &quot;SINGLE_DEVICE_STATUS_UNKNOWN_ERROR&quot; |
| OTHER_ERROR | &quot;SINGLE_DEVICE_STATUS_OTHER_ERROR&quot; |
| SUCCESS | &quot;SINGLE_DEVICE_STATUS_SUCCESS&quot; |
| PERMISSION_DENIED | &quot;SINGLE_DEVICE_STATUS_PERMISSION_DENIED&quot; |
| INVALID_DEVICE_IDENTIFIER | &quot;SINGLE_DEVICE_STATUS_INVALID_DEVICE_IDENTIFIER&quot; |
| INVALID_SECTION_TYPE | &quot;SINGLE_DEVICE_STATUS_INVALID_SECTION_TYPE&quot; |
| SECTION_NOT_YOURS | &quot;SINGLE_DEVICE_STATUS_SECTION_NOT_YOURS&quot; |
| INVALID_TOKEN | &quot;SINGLE_DEVICE_STATUS_INVALID_TOKEN&quot; |
| REVOKED_TOKEN | &quot;SINGLE_DEVICE_STATUS_REVOKED_TOKEN&quot; |
| DEVICE_LIMIT_EXCEEDED | &quot;SINGLE_DEVICE_STATUS_DEVICE_LIMIT_EXCEEDED&quot; |



