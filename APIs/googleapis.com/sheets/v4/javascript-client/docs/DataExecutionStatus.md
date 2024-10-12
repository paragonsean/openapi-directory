# GoogleSheetsApi.DataExecutionStatus

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errorCode** | **String** | The error code. | [optional] 
**errorMessage** | **String** | The error message, which may be empty. | [optional] 
**lastRefreshTime** | **String** | Gets the time the data last successfully refreshed. | [optional] 
**state** | **String** | The state of the data execution. | [optional] 



## Enum: ErrorCodeEnum


* `DATA_EXECUTION_ERROR_CODE_UNSPECIFIED` (value: `"DATA_EXECUTION_ERROR_CODE_UNSPECIFIED"`)

* `TIMED_OUT` (value: `"TIMED_OUT"`)

* `TOO_MANY_ROWS` (value: `"TOO_MANY_ROWS"`)

* `TOO_MANY_COLUMNS` (value: `"TOO_MANY_COLUMNS"`)

* `TOO_MANY_CELLS` (value: `"TOO_MANY_CELLS"`)

* `ENGINE` (value: `"ENGINE"`)

* `PARAMETER_INVALID` (value: `"PARAMETER_INVALID"`)

* `UNSUPPORTED_DATA_TYPE` (value: `"UNSUPPORTED_DATA_TYPE"`)

* `DUPLICATE_COLUMN_NAMES` (value: `"DUPLICATE_COLUMN_NAMES"`)

* `INTERRUPTED` (value: `"INTERRUPTED"`)

* `CONCURRENT_QUERY` (value: `"CONCURRENT_QUERY"`)

* `OTHER` (value: `"OTHER"`)

* `TOO_MANY_CHARS_PER_CELL` (value: `"TOO_MANY_CHARS_PER_CELL"`)

* `DATA_NOT_FOUND` (value: `"DATA_NOT_FOUND"`)

* `PERMISSION_DENIED` (value: `"PERMISSION_DENIED"`)

* `MISSING_COLUMN_ALIAS` (value: `"MISSING_COLUMN_ALIAS"`)

* `OBJECT_NOT_FOUND` (value: `"OBJECT_NOT_FOUND"`)

* `OBJECT_IN_ERROR_STATE` (value: `"OBJECT_IN_ERROR_STATE"`)

* `OBJECT_SPEC_INVALID` (value: `"OBJECT_SPEC_INVALID"`)





## Enum: StateEnum


* `DATA_EXECUTION_STATE_UNSPECIFIED` (value: `"DATA_EXECUTION_STATE_UNSPECIFIED"`)

* `NOT_STARTED` (value: `"NOT_STARTED"`)

* `RUNNING` (value: `"RUNNING"`)

* `SUCCEEDED` (value: `"SUCCEEDED"`)

* `FAILED` (value: `"FAILED"`)




