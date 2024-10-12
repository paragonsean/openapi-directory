# NewsSearchClient.Error

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **String** | The error code that identifies the category of error. | [default to &#39;None&#39;]
**message** | **String** | A description of the error. | 
**moreDetails** | **String** | A description that provides additional information about the error. | [optional] [readonly] 
**parameter** | **String** | The parameter in the request that caused the error. | [optional] [readonly] 
**subCode** | **String** | The error code that further helps to identify the error. | [optional] [readonly] 
**value** | **String** | The parameter&#39;s value in the request that was not valid. | [optional] [readonly] 



## Enum: CodeEnum


* `None` (value: `"None"`)

* `ServerError` (value: `"ServerError"`)

* `InvalidRequest` (value: `"InvalidRequest"`)

* `RateLimitExceeded` (value: `"RateLimitExceeded"`)

* `InvalidAuthorization` (value: `"InvalidAuthorization"`)

* `InsufficientAuthorization` (value: `"InsufficientAuthorization"`)





## Enum: SubCodeEnum


* `UnexpectedError` (value: `"UnexpectedError"`)

* `ResourceError` (value: `"ResourceError"`)

* `NotImplemented` (value: `"NotImplemented"`)

* `ParameterMissing` (value: `"ParameterMissing"`)

* `ParameterInvalidValue` (value: `"ParameterInvalidValue"`)

* `HttpNotAllowed` (value: `"HttpNotAllowed"`)

* `Blocked` (value: `"Blocked"`)

* `AuthorizationMissing` (value: `"AuthorizationMissing"`)

* `AuthorizationRedundancy` (value: `"AuthorizationRedundancy"`)

* `AuthorizationDisabled` (value: `"AuthorizationDisabled"`)

* `AuthorizationExpired` (value: `"AuthorizationExpired"`)




