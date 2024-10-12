

# LineProtocolError


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**code** | [**CodeEnum**](#CodeEnum) | Code is the machine-readable error code. |  [readonly] |
|**err** | **String** | Err is a stack of errors that occurred during processing of the request. Useful for debugging. |  [readonly] |
|**line** | **Integer** | First line within sent body containing malformed data |  [optional] [readonly] |
|**message** | **String** | Message is a human-readable message. |  [readonly] |
|**op** | **String** | Op describes the logical code operation during error. Useful for debugging. |  [readonly] |



## Enum: CodeEnum

| Name | Value |
|---- | -----|
| INTERNAL_ERROR | &quot;internal error&quot; |
| NOT_FOUND | &quot;not found&quot; |
| CONFLICT | &quot;conflict&quot; |
| INVALID | &quot;invalid&quot; |
| EMPTY_VALUE | &quot;empty value&quot; |
| UNAVAILABLE | &quot;unavailable&quot; |



