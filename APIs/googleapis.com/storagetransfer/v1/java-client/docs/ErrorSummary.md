

# ErrorSummary

A summary of errors by error code, plus a count and sample error log entries.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**errorCode** | [**ErrorCodeEnum**](#ErrorCodeEnum) | Required. |  [optional] |
|**errorCount** | **String** | Required. Count of this type of error. |  [optional] |
|**errorLogEntries** | [**List&lt;ErrorLogEntry&gt;**](ErrorLogEntry.md) | Error samples. At most 5 error log entries are recorded for a given error code for a single transfer operation. |  [optional] |



## Enum: ErrorCodeEnum

| Name | Value |
|---- | -----|
| OK | &quot;OK&quot; |
| CANCELLED | &quot;CANCELLED&quot; |
| UNKNOWN | &quot;UNKNOWN&quot; |
| INVALID_ARGUMENT | &quot;INVALID_ARGUMENT&quot; |
| DEADLINE_EXCEEDED | &quot;DEADLINE_EXCEEDED&quot; |
| NOT_FOUND | &quot;NOT_FOUND&quot; |
| ALREADY_EXISTS | &quot;ALREADY_EXISTS&quot; |
| PERMISSION_DENIED | &quot;PERMISSION_DENIED&quot; |
| UNAUTHENTICATED | &quot;UNAUTHENTICATED&quot; |
| RESOURCE_EXHAUSTED | &quot;RESOURCE_EXHAUSTED&quot; |
| FAILED_PRECONDITION | &quot;FAILED_PRECONDITION&quot; |
| ABORTED | &quot;ABORTED&quot; |
| OUT_OF_RANGE | &quot;OUT_OF_RANGE&quot; |
| UNIMPLEMENTED | &quot;UNIMPLEMENTED&quot; |
| INTERNAL | &quot;INTERNAL&quot; |
| UNAVAILABLE | &quot;UNAVAILABLE&quot; |
| DATA_LOSS | &quot;DATA_LOSS&quot; |



