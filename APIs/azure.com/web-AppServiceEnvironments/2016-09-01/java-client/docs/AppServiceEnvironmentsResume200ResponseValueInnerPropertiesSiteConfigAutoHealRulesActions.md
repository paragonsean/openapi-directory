

# AppServiceEnvironmentsResume200ResponseValueInnerPropertiesSiteConfigAutoHealRulesActions

Actions which to take by the auto-heal module when a rule is triggered.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**actionType** | [**ActionTypeEnum**](#ActionTypeEnum) | Predefined action to be taken. |  [optional] |
|**customAction** | [**AppServiceEnvironmentsResume200ResponseValueInnerPropertiesSiteConfigAutoHealRulesActionsCustomAction**](AppServiceEnvironmentsResume200ResponseValueInnerPropertiesSiteConfigAutoHealRulesActionsCustomAction.md) |  |  [optional] |
|**minProcessExecutionTime** | **String** | Minimum time the process must execute before taking the action |  [optional] |



## Enum: ActionTypeEnum

| Name | Value |
|---- | -----|
| RECYCLE | &quot;Recycle&quot; |
| LOG_EVENT | &quot;LogEvent&quot; |
| CUSTOM_ACTION | &quot;CustomAction&quot; |



