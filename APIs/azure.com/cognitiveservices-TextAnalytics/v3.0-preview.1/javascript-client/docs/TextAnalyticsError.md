# TextAnalyticsClient.TextAnalyticsError

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **String** | Error code. | 
**details** | [**[TextAnalyticsError]**](TextAnalyticsError.md) | Details about specific errors that led to this reported error. | [optional] 
**innerError** | [**InnerError**](InnerError.md) |  | [optional] 
**message** | **String** | Error message. | 
**target** | **String** | Error target. | [optional] 



## Enum: CodeEnum


* `invalidRequest` (value: `"invalidRequest"`)

* `invalidArgument` (value: `"invalidArgument"`)

* `internalServerError` (value: `"internalServerError"`)

* `serviceUnavailable` (value: `"serviceUnavailable"`)




