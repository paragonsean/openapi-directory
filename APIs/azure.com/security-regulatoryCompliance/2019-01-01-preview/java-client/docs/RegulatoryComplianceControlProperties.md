

# RegulatoryComplianceControlProperties

Regulatory compliance control data

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | The description of the regulatory compliance control |  [optional] [readonly] |
|**failedAssessments** | **Integer** | The number of supported regulatory compliance assessments of the given control with a failed state |  [optional] [readonly] |
|**passedAssessments** | **Integer** | The number of supported regulatory compliance assessments of the given control with a passed state |  [optional] [readonly] |
|**skippedAssessments** | **Integer** | The number of supported regulatory compliance assessments of the given control with a skipped state |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | Aggregative state based on the control&#39;s supported assessments states |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| PASSED | &quot;Passed&quot; |
| FAILED | &quot;Failed&quot; |
| SKIPPED | &quot;Skipped&quot; |
| UNSUPPORTED | &quot;Unsupported&quot; |



