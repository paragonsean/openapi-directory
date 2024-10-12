

# AutoHealActions

AutoHealActions - Describes the actions which can be              taken by the auto-heal module when a rule is triggered.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**actionType** | [**ActionTypeEnum**](#ActionTypeEnum) | ActionType - predefined action to be taken |  |
|**customAction** | [**AutoHealCustomAction**](AutoHealCustomAction.md) |  |  [optional] |
|**minProcessExecutionTime** | **String** | MinProcessExecutionTime - minimum time the process must execute              before taking the action |  [optional] |



## Enum: ActionTypeEnum

| Name | Value |
|---- | -----|
| RECYCLE | &quot;Recycle&quot; |
| LOG_EVENT | &quot;LogEvent&quot; |
| CUSTOM_ACTION | &quot;CustomAction&quot; |



