# InfluxOssApiService.Error

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **String** | code is the machine-readable error code. | [readonly] 
**err** | **String** | err is a stack of errors that occurred during processing of the request. Useful for debugging. | [optional] [readonly] 
**message** | **String** | message is a human-readable message. | [readonly] 
**op** | **String** | op describes the logical code operation during error. Useful for debugging. | [optional] [readonly] 



## Enum: CodeEnum


* `internal error` (value: `"internal error"`)

* `not found` (value: `"not found"`)

* `conflict` (value: `"conflict"`)

* `invalid` (value: `"invalid"`)

* `unprocessable entity` (value: `"unprocessable entity"`)

* `empty value` (value: `"empty value"`)

* `unavailable` (value: `"unavailable"`)

* `forbidden` (value: `"forbidden"`)

* `too many requests` (value: `"too many requests"`)

* `unauthorized` (value: `"unauthorized"`)

* `method not allowed` (value: `"method not allowed"`)

* `request too large` (value: `"request too large"`)

* `unsupported media type` (value: `"unsupported media type"`)




