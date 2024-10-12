

# StatusMessage


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**connectionClosed** | **Boolean** | Is the connection now closed |  [optional] |
|**connectionId** | **String** | The connection id |  [optional] |
|**connectionsAvailable** | **Integer** | The number of connections available for this account at this moment in time. Present on responses to Authentication messages only. |  [optional] |
|**errorCode** | [**ErrorCodeEnum**](#ErrorCodeEnum) | The type of error in case of a failure |  [optional] |
|**errorMessage** | **String** | Additional message in case of a failure |  [optional] |
|**statusCode** | [**StatusCodeEnum**](#StatusCodeEnum) | The status of the last request |  [optional] |



## Enum: ErrorCodeEnum

| Name | Value |
|---- | -----|
| NO_APP_KEY | &quot;NO_APP_KEY&quot; |
| INVALID_APP_KEY | &quot;INVALID_APP_KEY&quot; |
| NO_SESSION | &quot;NO_SESSION&quot; |
| INVALID_SESSION_INFORMATION | &quot;INVALID_SESSION_INFORMATION&quot; |
| NOT_AUTHORIZED | &quot;NOT_AUTHORIZED&quot; |
| INVALID_INPUT | &quot;INVALID_INPUT&quot; |
| INVALID_CLOCK | &quot;INVALID_CLOCK&quot; |
| UNEXPECTED_ERROR | &quot;UNEXPECTED_ERROR&quot; |
| TIMEOUT | &quot;TIMEOUT&quot; |
| SUBSCRIPTION_LIMIT_EXCEEDED | &quot;SUBSCRIPTION_LIMIT_EXCEEDED&quot; |
| INVALID_REQUEST | &quot;INVALID_REQUEST&quot; |
| CONNECTION_FAILED | &quot;CONNECTION_FAILED&quot; |
| MAX_CONNECTION_LIMIT_EXCEEDED | &quot;MAX_CONNECTION_LIMIT_EXCEEDED&quot; |
| TOO_MANY_REQUESTS | &quot;TOO_MANY_REQUESTS&quot; |



## Enum: StatusCodeEnum

| Name | Value |
|---- | -----|
| SUCCESS | &quot;SUCCESS&quot; |
| FAILURE | &quot;FAILURE&quot; |



