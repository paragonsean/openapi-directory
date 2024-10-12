# CloudSearchApi.RepositoryError

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errorMessage** | **String** | Message that describes the error. The maximum allowable length of the message is 8192 characters. | [optional] 
**httpStatusCode** | **Number** | Error codes. Matches the definition of HTTP status codes. | [optional] 
**type** | **String** | The type of error. | [optional] 



## Enum: TypeEnum


* `UNKNOWN` (value: `"UNKNOWN"`)

* `NETWORK_ERROR` (value: `"NETWORK_ERROR"`)

* `DNS_ERROR` (value: `"DNS_ERROR"`)

* `CONNECTION_ERROR` (value: `"CONNECTION_ERROR"`)

* `AUTHENTICATION_ERROR` (value: `"AUTHENTICATION_ERROR"`)

* `AUTHORIZATION_ERROR` (value: `"AUTHORIZATION_ERROR"`)

* `SERVER_ERROR` (value: `"SERVER_ERROR"`)

* `QUOTA_EXCEEDED` (value: `"QUOTA_EXCEEDED"`)

* `SERVICE_UNAVAILABLE` (value: `"SERVICE_UNAVAILABLE"`)

* `CLIENT_ERROR` (value: `"CLIENT_ERROR"`)




