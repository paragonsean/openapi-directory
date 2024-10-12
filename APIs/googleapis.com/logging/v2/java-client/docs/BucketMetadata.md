

# BucketMetadata

Metadata for LongRunningUpdateBucket Operations.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createBucketRequest** | [**CreateBucketRequest**](CreateBucketRequest.md) |  |  [optional] |
|**endTime** | **String** | The end time of an operation. |  [optional] |
|**startTime** | **String** | The create time of an operation. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Output only. State of an operation. |  [optional] [readonly] |
|**updateBucketRequest** | [**UpdateBucketRequest**](UpdateBucketRequest.md) |  |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;OPERATION_STATE_UNSPECIFIED&quot; |
| SCHEDULED | &quot;OPERATION_STATE_SCHEDULED&quot; |
| WAITING_FOR_PERMISSIONS | &quot;OPERATION_STATE_WAITING_FOR_PERMISSIONS&quot; |
| RUNNING | &quot;OPERATION_STATE_RUNNING&quot; |
| SUCCEEDED | &quot;OPERATION_STATE_SUCCEEDED&quot; |
| FAILED | &quot;OPERATION_STATE_FAILED&quot; |
| CANCELLED | &quot;OPERATION_STATE_CANCELLED&quot; |
| PENDING | &quot;OPERATION_STATE_PENDING&quot; |



