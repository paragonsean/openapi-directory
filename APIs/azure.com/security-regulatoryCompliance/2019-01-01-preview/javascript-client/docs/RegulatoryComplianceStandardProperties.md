# SecurityCenter.RegulatoryComplianceStandardProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**failedControls** | **Number** | The number of supported regulatory compliance controls of the given standard with a failed state | [optional] [readonly] 
**passedControls** | **Number** | The number of supported regulatory compliance controls of the given standard with a passed state | [optional] [readonly] 
**skippedControls** | **Number** | The number of supported regulatory compliance controls of the given standard with a skipped state | [optional] [readonly] 
**state** | **String** | Aggregative state based on the standard&#39;s supported controls states | [optional] 
**unsupportedControls** | **Number** | The number of regulatory compliance controls of the given standard which are unsupported by automated assessments | [optional] [readonly] 



## Enum: StateEnum


* `Passed` (value: `"Passed"`)

* `Failed` (value: `"Failed"`)

* `Skipped` (value: `"Skipped"`)

* `Unsupported` (value: `"Unsupported"`)




