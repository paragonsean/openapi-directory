

# AutopilotCompatibilityIssue

AutopilotCompatibilityIssue contains information about a specific compatibility issue with Autopilot mode.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**constraintType** | **String** | The constraint type of the issue. |  [optional] |
|**description** | **String** | The description of the issue. |  [optional] |
|**documentationUrl** | **String** | A URL to a public documnetation, which addresses resolving this issue. |  [optional] |
|**incompatibilityType** | [**IncompatibilityTypeEnum**](#IncompatibilityTypeEnum) | The incompatibility type of this issue. |  [optional] |
|**lastObservation** | **String** | The last time when this issue was observed. |  [optional] |
|**subjects** | **List&lt;String&gt;** | The name of the resources which are subject to this issue. |  [optional] |



## Enum: IncompatibilityTypeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;UNSPECIFIED&quot; |
| INCOMPATIBILITY | &quot;INCOMPATIBILITY&quot; |
| ADDITIONAL_CONFIG_REQUIRED | &quot;ADDITIONAL_CONFIG_REQUIRED&quot; |
| PASSED_WITH_OPTIONAL_CONFIG | &quot;PASSED_WITH_OPTIONAL_CONFIG&quot; |



