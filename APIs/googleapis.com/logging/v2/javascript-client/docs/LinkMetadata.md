# CloudLoggingApi.LinkMetadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createLinkRequest** | [**CreateLinkRequest**](CreateLinkRequest.md) |  | [optional] 
**deleteLinkRequest** | [**DeleteLinkRequest**](DeleteLinkRequest.md) |  | [optional] 
**endTime** | **String** | The end time of an operation. | [optional] 
**startTime** | **String** | The start time of an operation. | [optional] 
**state** | **String** | Output only. State of an operation. | [optional] [readonly] 



## Enum: StateEnum


* `UNSPECIFIED` (value: `"OPERATION_STATE_UNSPECIFIED"`)

* `SCHEDULED` (value: `"OPERATION_STATE_SCHEDULED"`)

* `WAITING_FOR_PERMISSIONS` (value: `"OPERATION_STATE_WAITING_FOR_PERMISSIONS"`)

* `RUNNING` (value: `"OPERATION_STATE_RUNNING"`)

* `SUCCEEDED` (value: `"OPERATION_STATE_SUCCEEDED"`)

* `FAILED` (value: `"OPERATION_STATE_FAILED"`)

* `CANCELLED` (value: `"OPERATION_STATE_CANCELLED"`)

* `PENDING` (value: `"OPERATION_STATE_PENDING"`)




