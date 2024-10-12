# ApigeeApi.GoogleCloudApigeeV1UpdateError

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **String** | Status code. | [optional] 
**message** | **String** | User-friendly error message. | [optional] 
**resource** | **String** | The sub resource specific to this error (e.g. a proxy deployed within the EnvironmentConfig). If empty the error refers to the top level resource. | [optional] 
**type** | **String** | A string that uniquely identifies the type of error. This provides a more reliable means to deduplicate errors across revisions and instances. | [optional] 



## Enum: CodeEnum


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




