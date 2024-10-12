

# GoogleCloudApigeeV1UpdateError

Details on why a resource update failed in the runtime.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**code** | [**CodeEnum**](#CodeEnum) | Status code. |  [optional] |
|**message** | **String** | User-friendly error message. |  [optional] |
|**resource** | **String** | The sub resource specific to this error (e.g. a proxy deployed within the EnvironmentConfig). If empty the error refers to the top level resource. |  [optional] |
|**type** | **String** | A string that uniquely identifies the type of error. This provides a more reliable means to deduplicate errors across revisions and instances. |  [optional] |



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



