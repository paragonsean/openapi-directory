# CloudLoggingApi.CopyLogEntriesMetadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cancellationRequested** | **Boolean** | Identifies whether the user has requested cancellation of the operation. | [optional] 
**destination** | **String** | Destination to which to copy log entries.For example, a Cloud Storage bucket:\&quot;storage.googleapis.com/my-cloud-storage-bucket\&quot; | [optional] 
**endTime** | **String** | The end time of an operation. | [optional] 
**progress** | **Number** | Estimated progress of the operation (0 - 100%). | [optional] 
**request** | [**CopyLogEntriesRequest**](CopyLogEntriesRequest.md) |  | [optional] 
**source** | **String** | Source from which to copy log entries.For example, a log bucket:\&quot;projects/my-project/locations/global/buckets/my-source-bucket\&quot; | [optional] 
**startTime** | **String** | The create time of an operation. | [optional] 
**state** | **String** | Output only. State of an operation. | [optional] [readonly] 
**verb** | **String** | Name of the verb executed by the operation.For example,\&quot;copy\&quot; | [optional] 
**writerIdentity** | **String** | The IAM identity of a service account that must be granted access to the destination.If the service account is not granted permission to the destination within an hour, the operation will be cancelled.For example: \&quot;serviceAccount:foo@bar.com\&quot; | [optional] 



## Enum: StateEnum


* `UNSPECIFIED` (value: `"OPERATION_STATE_UNSPECIFIED"`)

* `SCHEDULED` (value: `"OPERATION_STATE_SCHEDULED"`)

* `WAITING_FOR_PERMISSIONS` (value: `"OPERATION_STATE_WAITING_FOR_PERMISSIONS"`)

* `RUNNING` (value: `"OPERATION_STATE_RUNNING"`)

* `SUCCEEDED` (value: `"OPERATION_STATE_SUCCEEDED"`)

* `FAILED` (value: `"OPERATION_STATE_FAILED"`)

* `CANCELLED` (value: `"OPERATION_STATE_CANCELLED"`)

* `PENDING` (value: `"OPERATION_STATE_PENDING"`)




