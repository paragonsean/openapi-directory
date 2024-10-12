# SecurityCenter.RegulatoryComplianceAssessmentProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assessmentDetailsLink** | **String** | Link to more detailed assessment results data. The response type will be according to the assessmentType field | [optional] [readonly] 
**assessmentType** | **String** | The expected type of assessment contained in the AssessmentDetailsLink | [optional] [readonly] 
**description** | **String** | The description of the regulatory compliance assessment | [optional] [readonly] 
**failedResources** | **Number** | The given assessment&#39;s related resources count with failed state. | [optional] [readonly] 
**passedResources** | **Number** | The given assessment&#39;s related resources count with passed state. | [optional] [readonly] 
**skippedResources** | **Number** | The given assessment&#39;s related resources count with skipped state. | [optional] [readonly] 
**state** | **String** | Aggregative state based on the assessment&#39;s scanned resources states | [optional] 
**unsupportedResources** | **Number** | The given assessment&#39;s related resources count with unsupported state. | [optional] [readonly] 



## Enum: StateEnum


* `Passed` (value: `"Passed"`)

* `Failed` (value: `"Failed"`)

* `Skipped` (value: `"Skipped"`)

* `Unsupported` (value: `"Unsupported"`)




