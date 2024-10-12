

# DataExecutionStatus

The data execution status. A data execution is created to sync a data source object with the latest data from a DataSource. It is usually scheduled to run at background, you can check its state to tell if an execution completes There are several scenarios where a data execution is triggered to run: * Adding a data source creates an associated data source sheet as well as a data execution to sync the data from the data source to the sheet. * Updating a data source creates a data execution to refresh the associated data source sheet similarly. * You can send refresh request to explicitly refresh one or multiple data source objects.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**errorCode** | [**ErrorCodeEnum**](#ErrorCodeEnum) | The error code. |  [optional] |
|**errorMessage** | **String** | The error message, which may be empty. |  [optional] |
|**lastRefreshTime** | **String** | Gets the time the data last successfully refreshed. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | The state of the data execution. |  [optional] |



## Enum: ErrorCodeEnum

| Name | Value |
|---- | -----|
| DATA_EXECUTION_ERROR_CODE_UNSPECIFIED | &quot;DATA_EXECUTION_ERROR_CODE_UNSPECIFIED&quot; |
| TIMED_OUT | &quot;TIMED_OUT&quot; |
| TOO_MANY_ROWS | &quot;TOO_MANY_ROWS&quot; |
| TOO_MANY_COLUMNS | &quot;TOO_MANY_COLUMNS&quot; |
| TOO_MANY_CELLS | &quot;TOO_MANY_CELLS&quot; |
| ENGINE | &quot;ENGINE&quot; |
| PARAMETER_INVALID | &quot;PARAMETER_INVALID&quot; |
| UNSUPPORTED_DATA_TYPE | &quot;UNSUPPORTED_DATA_TYPE&quot; |
| DUPLICATE_COLUMN_NAMES | &quot;DUPLICATE_COLUMN_NAMES&quot; |
| INTERRUPTED | &quot;INTERRUPTED&quot; |
| CONCURRENT_QUERY | &quot;CONCURRENT_QUERY&quot; |
| OTHER | &quot;OTHER&quot; |
| TOO_MANY_CHARS_PER_CELL | &quot;TOO_MANY_CHARS_PER_CELL&quot; |
| DATA_NOT_FOUND | &quot;DATA_NOT_FOUND&quot; |
| PERMISSION_DENIED | &quot;PERMISSION_DENIED&quot; |
| MISSING_COLUMN_ALIAS | &quot;MISSING_COLUMN_ALIAS&quot; |
| OBJECT_NOT_FOUND | &quot;OBJECT_NOT_FOUND&quot; |
| OBJECT_IN_ERROR_STATE | &quot;OBJECT_IN_ERROR_STATE&quot; |
| OBJECT_SPEC_INVALID | &quot;OBJECT_SPEC_INVALID&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| DATA_EXECUTION_STATE_UNSPECIFIED | &quot;DATA_EXECUTION_STATE_UNSPECIFIED&quot; |
| NOT_STARTED | &quot;NOT_STARTED&quot; |
| RUNNING | &quot;RUNNING&quot; |
| SUCCEEDED | &quot;SUCCEEDED&quot; |
| FAILED | &quot;FAILED&quot; |



