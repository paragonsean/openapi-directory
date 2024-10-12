

# FailedEvent

An event generated when the execution of a pipeline has failed. Note that other events can continue to occur after this event.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cause** | **String** | The human-readable description of the cause of the failure. |  [optional] |
|**code** | [**CodeEnum**](#CodeEnum) | The Google standard error code that best describes this failure. |  [optional] |



## Enum: CodeEnum

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



