

# TextAnalyticsError


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**code** | [**CodeEnum**](#CodeEnum) | Error code. |  |
|**details** | [**List&lt;TextAnalyticsError&gt;**](TextAnalyticsError.md) | Details about specific errors that led to this reported error. |  [optional] |
|**innerError** | [**InnerError**](InnerError.md) |  |  [optional] |
|**message** | **String** | Error message. |  |
|**target** | **String** | Error target. |  [optional] |



## Enum: CodeEnum

| Name | Value |
|---- | -----|
| INVALID_REQUEST | &quot;invalidRequest&quot; |
| INVALID_ARGUMENT | &quot;invalidArgument&quot; |
| INTERNAL_SERVER_ERROR | &quot;internalServerError&quot; |
| SERVICE_UNAVAILABLE | &quot;serviceUnavailable&quot; |



