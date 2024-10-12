

# ValidationCheck

ValidationCheck represents the result of preflight check.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**option** | [**OptionEnum**](#OptionEnum) | Options used for the validation check |  [optional] |
|**scenario** | [**ScenarioEnum**](#ScenarioEnum) | Output only. The scenario when the preflight checks were run. |  [optional] [readonly] |
|**status** | [**ValidationCheckStatus**](ValidationCheckStatus.md) |  |  [optional] |



## Enum: OptionEnum

| Name | Value |
|---- | -----|
| OPTIONS_UNSPECIFIED | &quot;OPTIONS_UNSPECIFIED&quot; |
| SKIP_VALIDATION_CHECK_BLOCKING | &quot;SKIP_VALIDATION_CHECK_BLOCKING&quot; |
| SKIP_VALIDATION_ALL | &quot;SKIP_VALIDATION_ALL&quot; |



## Enum: ScenarioEnum

| Name | Value |
|---- | -----|
| SCENARIO_UNSPECIFIED | &quot;SCENARIO_UNSPECIFIED&quot; |
| CREATE | &quot;CREATE&quot; |
| UPDATE | &quot;UPDATE&quot; |



