# DatastreamApi.Validation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **String** | A custom code identifying this validation. | [optional] 
**description** | **String** | A short description of the validation. | [optional] 
**message** | [**[ValidationMessage]**](ValidationMessage.md) | Messages reflecting the validation results. | [optional] 
**state** | **String** | Output only. Validation execution status. | [optional] [readonly] 



## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `NOT_EXECUTED` (value: `"NOT_EXECUTED"`)

* `FAILED` (value: `"FAILED"`)

* `PASSED` (value: `"PASSED"`)

* `WARNING` (value: `"WARNING"`)




