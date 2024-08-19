# AutoSuggestClient.Error

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **String** |  | 
**code** | **String** | The error code that identifies the category of error. | [default to &#39;None&#39;]
**message** | **String** | A description of the error. | 
**moreDetails** | **String** | A description that provides additional information about the error. | [optional] [readonly] 
**parameter** | **String** | The parameter in the request that caused the error. | [optional] [readonly] 
**value** | **String** | The parameter&#39;s value in the request that was not valid. | [optional] [readonly] 



## Enum: CodeEnum


* `None` (value: `"None"`)

* `ServerError` (value: `"ServerError"`)

* `InvalidRequest` (value: `"InvalidRequest"`)

* `RateLimitExceeded` (value: `"RateLimitExceeded"`)

* `InvalidAuthorization` (value: `"InvalidAuthorization"`)

* `InsufficientAuthorization` (value: `"InsufficientAuthorization"`)




