

# ActionStatus

Represents the status for a request to either invoke or submit a [dialog](https://developers.google.com/chat/how-tos/dialogs).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**statusCode** | [**StatusCodeEnum**](#StatusCodeEnum) | The status code. |  [optional] |
|**userFacingMessage** | **String** | The message to send users about the status of their request. If unset, a generic message based on the &#x60;status_code&#x60; is sent. |  [optional] |



## Enum: StatusCodeEnum

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



