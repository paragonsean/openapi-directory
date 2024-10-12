# BetfairExchangeStreamingApi.StatusMessage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connectionClosed** | **Boolean** | Is the connection now closed | [optional] 
**connectionId** | **String** | The connection id | [optional] 
**connectionsAvailable** | **Number** | The number of connections available for this account at this moment in time. Present on responses to Authentication messages only. | [optional] 
**errorCode** | **String** | The type of error in case of a failure | [optional] 
**errorMessage** | **String** | Additional message in case of a failure | [optional] 
**statusCode** | **String** | The status of the last request | [optional] 



## Enum: ErrorCodeEnum


* `NO_APP_KEY` (value: `"NO_APP_KEY"`)

* `INVALID_APP_KEY` (value: `"INVALID_APP_KEY"`)

* `NO_SESSION` (value: `"NO_SESSION"`)

* `INVALID_SESSION_INFORMATION` (value: `"INVALID_SESSION_INFORMATION"`)

* `NOT_AUTHORIZED` (value: `"NOT_AUTHORIZED"`)

* `INVALID_INPUT` (value: `"INVALID_INPUT"`)

* `INVALID_CLOCK` (value: `"INVALID_CLOCK"`)

* `UNEXPECTED_ERROR` (value: `"UNEXPECTED_ERROR"`)

* `TIMEOUT` (value: `"TIMEOUT"`)

* `SUBSCRIPTION_LIMIT_EXCEEDED` (value: `"SUBSCRIPTION_LIMIT_EXCEEDED"`)

* `INVALID_REQUEST` (value: `"INVALID_REQUEST"`)

* `CONNECTION_FAILED` (value: `"CONNECTION_FAILED"`)

* `MAX_CONNECTION_LIMIT_EXCEEDED` (value: `"MAX_CONNECTION_LIMIT_EXCEEDED"`)

* `TOO_MANY_REQUESTS` (value: `"TOO_MANY_REQUESTS"`)





## Enum: StatusCodeEnum


* `SUCCESS` (value: `"SUCCESS"`)

* `FAILURE` (value: `"FAILURE"`)




