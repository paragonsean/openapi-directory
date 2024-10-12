

# Error


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**code** | [**CodeEnum**](#CodeEnum) | code is the machine-readable error code. |  [readonly] |
|**err** | **String** | err is a stack of errors that occurred during processing of the request. Useful for debugging. |  [optional] [readonly] |
|**message** | **String** | message is a human-readable message. |  [readonly] |
|**op** | **String** | op describes the logical code operation during error. Useful for debugging. |  [optional] [readonly] |



## Enum: CodeEnum

| Name | Value |
|---- | -----|
| INTERNAL_ERROR | &quot;internal error&quot; |
| NOT_FOUND | &quot;not found&quot; |
| CONFLICT | &quot;conflict&quot; |
| INVALID | &quot;invalid&quot; |
| UNPROCESSABLE_ENTITY | &quot;unprocessable entity&quot; |
| EMPTY_VALUE | &quot;empty value&quot; |
| UNAVAILABLE | &quot;unavailable&quot; |
| FORBIDDEN | &quot;forbidden&quot; |
| TOO_MANY_REQUESTS | &quot;too many requests&quot; |
| UNAUTHORIZED | &quot;unauthorized&quot; |
| METHOD_NOT_ALLOWED | &quot;method not allowed&quot; |
| REQUEST_TOO_LARGE | &quot;request too large&quot; |
| UNSUPPORTED_MEDIA_TYPE | &quot;unsupported media type&quot; |



