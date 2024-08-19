

# Error

Defines the error that occurred.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**code** | [**CodeEnum**](#CodeEnum) | The error code that identifies the category of error. |  |
|**message** | **String** | A description of the error. |  |
|**moreDetails** | **String** | A description that provides additional information about the error. |  [optional] [readonly] |
|**parameter** | **String** | The parameter in the request that caused the error. |  [optional] [readonly] |
|**subCode** | [**SubCodeEnum**](#SubCodeEnum) | The error code that further helps to identify the error. |  [optional] [readonly] |
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



## Enum: SubCodeEnum

| Name | Value |
|---- | -----|
| UNEXPECTED_ERROR | &quot;UnexpectedError&quot; |
| RESOURCE_ERROR | &quot;ResourceError&quot; |
| NOT_IMPLEMENTED | &quot;NotImplemented&quot; |
| PARAMETER_MISSING | &quot;ParameterMissing&quot; |
| PARAMETER_INVALID_VALUE | &quot;ParameterInvalidValue&quot; |
| HTTP_NOT_ALLOWED | &quot;HttpNotAllowed&quot; |
| BLOCKED | &quot;Blocked&quot; |
| AUTHORIZATION_MISSING | &quot;AuthorizationMissing&quot; |
| AUTHORIZATION_REDUNDANCY | &quot;AuthorizationRedundancy&quot; |
| AUTHORIZATION_DISABLED | &quot;AuthorizationDisabled&quot; |
| AUTHORIZATION_EXPIRED | &quot;AuthorizationExpired&quot; |



