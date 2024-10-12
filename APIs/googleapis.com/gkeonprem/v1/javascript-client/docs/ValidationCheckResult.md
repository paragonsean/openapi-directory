# AnthosOnPremApi.ValidationCheckResult

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **String** | The category of the validation. | [optional] 
**description** | **String** | The description of the validation check. | [optional] 
**details** | **String** | Detailed failure information, which might be unformatted. | [optional] 
**reason** | **String** | A human-readable message of the check failure. | [optional] 
**state** | **String** | The validation check state. | [optional] 



## Enum: StateEnum


* `UNKNOWN` (value: `"STATE_UNKNOWN"`)

* `FAILURE` (value: `"STATE_FAILURE"`)

* `SKIPPED` (value: `"STATE_SKIPPED"`)

* `FATAL` (value: `"STATE_FATAL"`)

* `WARNING` (value: `"STATE_WARNING"`)




