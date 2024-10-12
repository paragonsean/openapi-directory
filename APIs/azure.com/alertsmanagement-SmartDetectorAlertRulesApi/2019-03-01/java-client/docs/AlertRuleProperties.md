

# AlertRuleProperties

The alert rule properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**actionGroups** | [**ActionGroupsInformation**](ActionGroupsInformation.md) |  |  |
|**description** | **String** | The alert rule description. |  [optional] |
|**detector** | [**Detector**](Detector.md) |  |  |
|**frequency** | **String** | The alert rule frequency in ISO8601 format. The time granularity must be in minutes and minimum value is 5 minutes. |  |
|**scope** | **List&lt;String&gt;** | The alert rule resources scope. |  |
|**severity** | [**SeverityEnum**](#SeverityEnum) | The alert rule severity. |  |
|**state** | [**StateEnum**](#StateEnum) | The alert rule state. |  |
|**throttling** | [**ThrottlingInformation**](ThrottlingInformation.md) |  |  [optional] |



## Enum: SeverityEnum

| Name | Value |
|---- | -----|
| SEV0 | &quot;Sev0&quot; |
| SEV1 | &quot;Sev1&quot; |
| SEV2 | &quot;Sev2&quot; |
| SEV3 | &quot;Sev3&quot; |
| SEV4 | &quot;Sev4&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| ENABLED | &quot;Enabled&quot; |
| DISABLED | &quot;Disabled&quot; |



