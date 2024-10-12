

# Error

Defines the error that occurred.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**type** | **String** |  |  |
|**code** | [**CodeEnum**](#CodeEnum) | The error code that identifies the category of error. |  |
|**message** | **String** | A description of the error. |  |
|**moreDetails** | **String** | A description that provides additional information about the error. |  [optional] [readonly] |
|**parameter** | **String** | The parameter in the request that caused the error. |  [optional] [readonly] |
|**value** | **String** | The parameter&#39;s value in the request that was not valid. |  [optional] [readonly] |



## Enum: CodeEnum

| Name | Value |
|---- | -----|
| NONE | &quot;None&quot; |
| SERVER_ERROR | &quot;ServerError&quot; |
| INVALID_REQUEST | &quot;InvalidRequest&quot; |
| RATE_LIMIT_EXCEEDED | &quot;RateLimitExceeded&quot; |
| INVALID_AUTHORIZATION | &quot;InvalidAuthorization&quot; |
| INSUFFICIENT_AUTHORIZATION | &quot;InsufficientAuthorization&quot; |



