# CloudLoggingApi.BucketMetadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createBucketRequest** | [**CreateBucketRequest**](CreateBucketRequest.md) |  | [optional] 
**endTime** | **String** | The end time of an operation. | [optional] 
**startTime** | **String** | The create time of an operation. | [optional] 
**state** | **String** | Output only. State of an operation. | [optional] [readonly] 
**updateBucketRequest** | [**UpdateBucketRequest**](UpdateBucketRequest.md) |  | [optional] 



## Enum: StateEnum


* `UNSPECIFIED` (value: `"OPERATION_STATE_UNSPECIFIED"`)

* `SCHEDULED` (value: `"OPERATION_STATE_SCHEDULED"`)

* `WAITING_FOR_PERMISSIONS` (value: `"OPERATION_STATE_WAITING_FOR_PERMISSIONS"`)

* `RUNNING` (value: `"OPERATION_STATE_RUNNING"`)

* `SUCCEEDED` (value: `"OPERATION_STATE_SUCCEEDED"`)

* `FAILED` (value: `"OPERATION_STATE_FAILED"`)

* `CANCELLED` (value: `"OPERATION_STATE_CANCELLED"`)

* `PENDING` (value: `"OPERATION_STATE_PENDING"`)




