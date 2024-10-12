# AndroidDeviceProvisioningPartnerApi.PerDeviceStatusInBatch

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deviceId** | **String** | If processing succeeds, the device ID of the device. | [optional] 
**errorIdentifier** | **String** | If processing fails, the error type. | [optional] 
**errorMessage** | **String** | If processing fails, a developer message explaining what went wrong. | [optional] 
**status** | **String** | The result status of the device after processing. | [optional] 



## Enum: StatusEnum


* `UNSPECIFIED` (value: `"SINGLE_DEVICE_STATUS_UNSPECIFIED"`)

* `UNKNOWN_ERROR` (value: `"SINGLE_DEVICE_STATUS_UNKNOWN_ERROR"`)

* `OTHER_ERROR` (value: `"SINGLE_DEVICE_STATUS_OTHER_ERROR"`)

* `SUCCESS` (value: `"SINGLE_DEVICE_STATUS_SUCCESS"`)

* `PERMISSION_DENIED` (value: `"SINGLE_DEVICE_STATUS_PERMISSION_DENIED"`)

* `INVALID_DEVICE_IDENTIFIER` (value: `"SINGLE_DEVICE_STATUS_INVALID_DEVICE_IDENTIFIER"`)

* `INVALID_SECTION_TYPE` (value: `"SINGLE_DEVICE_STATUS_INVALID_SECTION_TYPE"`)

* `SECTION_NOT_YOURS` (value: `"SINGLE_DEVICE_STATUS_SECTION_NOT_YOURS"`)

* `INVALID_TOKEN` (value: `"SINGLE_DEVICE_STATUS_INVALID_TOKEN"`)

* `REVOKED_TOKEN` (value: `"SINGLE_DEVICE_STATUS_REVOKED_TOKEN"`)

* `DEVICE_LIMIT_EXCEEDED` (value: `"SINGLE_DEVICE_STATUS_DEVICE_LIMIT_EXCEEDED"`)




