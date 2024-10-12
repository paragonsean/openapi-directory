

# CustomVoiceParams

Description of the custom voice to be synthesized.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**model** | **String** | Required. The name of the AutoML model that synthesizes the custom voice. |  [optional] |
|**reportedUsage** | [**ReportedUsageEnum**](#ReportedUsageEnum) | Optional. Deprecated. The usage of the synthesized audio to be reported. |  [optional] |



## Enum: ReportedUsageEnum

| Name | Value |
|---- | -----|
| REPORTED_USAGE_UNSPECIFIED | &quot;REPORTED_USAGE_UNSPECIFIED&quot; |
| REALTIME | &quot;REALTIME&quot; |
| OFFLINE | &quot;OFFLINE&quot; |



