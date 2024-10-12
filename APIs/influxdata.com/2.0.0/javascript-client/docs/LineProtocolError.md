# InfluxOssApiService.LineProtocolError

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **String** | Code is the machine-readable error code. | [readonly] 
**err** | **String** | Err is a stack of errors that occurred during processing of the request. Useful for debugging. | [readonly] 
**line** | **Number** | First line within sent body containing malformed data | [optional] [readonly] 
**message** | **String** | Message is a human-readable message. | [readonly] 
**op** | **String** | Op describes the logical code operation during error. Useful for debugging. | [readonly] 



## Enum: CodeEnum


* `internal error` (value: `"internal error"`)

* `not found` (value: `"not found"`)

* `conflict` (value: `"conflict"`)

* `invalid` (value: `"invalid"`)

* `empty value` (value: `"empty value"`)

* `unavailable` (value: `"unavailable"`)




