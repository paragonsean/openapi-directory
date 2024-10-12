# StorageTransferApi.ErrorSummary

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errorCode** | **String** | Required. | [optional] 
**errorCount** | **String** | Required. Count of this type of error. | [optional] 
**errorLogEntries** | [**[ErrorLogEntry]**](ErrorLogEntry.md) | Error samples. At most 5 error log entries are recorded for a given error code for a single transfer operation. | [optional] 



## Enum: ErrorCodeEnum


* `OK` (value: `"OK"`)

* `CANCELLED` (value: `"CANCELLED"`)

* `UNKNOWN` (value: `"UNKNOWN"`)

* `INVALID_ARGUMENT` (value: `"INVALID_ARGUMENT"`)

* `DEADLINE_EXCEEDED` (value: `"DEADLINE_EXCEEDED"`)

* `NOT_FOUND` (value: `"NOT_FOUND"`)

* `ALREADY_EXISTS` (value: `"ALREADY_EXISTS"`)

* `PERMISSION_DENIED` (value: `"PERMISSION_DENIED"`)

* `UNAUTHENTICATED` (value: `"UNAUTHENTICATED"`)

* `RESOURCE_EXHAUSTED` (value: `"RESOURCE_EXHAUSTED"`)

* `FAILED_PRECONDITION` (value: `"FAILED_PRECONDITION"`)

* `ABORTED` (value: `"ABORTED"`)

* `OUT_OF_RANGE` (value: `"OUT_OF_RANGE"`)

* `UNIMPLEMENTED` (value: `"UNIMPLEMENTED"`)

* `INTERNAL` (value: `"INTERNAL"`)

* `UNAVAILABLE` (value: `"UNAVAILABLE"`)

* `DATA_LOSS` (value: `"DATA_LOSS"`)




