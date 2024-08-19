

# RegulatoryComplianceAssessmentProperties

Regulatory compliance assessment data

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**assessmentDetailsLink** | **String** | Link to more detailed assessment results data. The response type will be according to the assessmentType field |  [optional] [readonly] |
|**assessmentType** | **String** | The expected type of assessment contained in the AssessmentDetailsLink |  [optional] [readonly] |
|**description** | **String** | The description of the regulatory compliance assessment |  [optional] [readonly] |
|**failedResources** | **Integer** | The given assessment&#39;s related resources count with failed state. |  [optional] [readonly] |
|**passedResources** | **Integer** | The given assessment&#39;s related resources count with passed state. |  [optional] [readonly] |
|**skippedResources** | **Integer** | The given assessment&#39;s related resources count with skipped state. |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | Aggregative state based on the assessment&#39;s scanned resources states |  [optional] |
|**unsupportedResources** | **Integer** | The given assessment&#39;s related resources count with unsupported state. |  [optional] [readonly] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| PASSED | &quot;Passed&quot; |
| FAILED | &quot;Failed&quot; |
| SKIPPED | &quot;Skipped&quot; |
| UNSUPPORTED | &quot;Unsupported&quot; |



