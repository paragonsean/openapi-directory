

# RegulatoryComplianceStandardProperties

Regulatory compliance standard data

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**failedControls** | **Integer** | The number of supported regulatory compliance controls of the given standard with a failed state |  [optional] [readonly] |
|**passedControls** | **Integer** | The number of supported regulatory compliance controls of the given standard with a passed state |  [optional] [readonly] |
|**skippedControls** | **Integer** | The number of supported regulatory compliance controls of the given standard with a skipped state |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | Aggregative state based on the standard&#39;s supported controls states |  [optional] |
|**unsupportedControls** | **Integer** | The number of regulatory compliance controls of the given standard which are unsupported by automated assessments |  [optional] [readonly] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| PASSED | &quot;Passed&quot; |
| FAILED | &quot;Failed&quot; |
| SKIPPED | &quot;Skipped&quot; |
| UNSUPPORTED | &quot;Unsupported&quot; |



