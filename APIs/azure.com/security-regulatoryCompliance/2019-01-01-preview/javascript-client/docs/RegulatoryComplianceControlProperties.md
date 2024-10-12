# SecurityCenter.RegulatoryComplianceControlProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **String** | The description of the regulatory compliance control | [optional] [readonly] 
**failedAssessments** | **Number** | The number of supported regulatory compliance assessments of the given control with a failed state | [optional] [readonly] 
**passedAssessments** | **Number** | The number of supported regulatory compliance assessments of the given control with a passed state | [optional] [readonly] 
**skippedAssessments** | **Number** | The number of supported regulatory compliance assessments of the given control with a skipped state | [optional] [readonly] 
**state** | **String** | Aggregative state based on the control&#39;s supported assessments states | [optional] 



## Enum: StateEnum


* `Passed` (value: `"Passed"`)

* `Failed` (value: `"Failed"`)

* `Skipped` (value: `"Skipped"`)

* `Unsupported` (value: `"Unsupported"`)




