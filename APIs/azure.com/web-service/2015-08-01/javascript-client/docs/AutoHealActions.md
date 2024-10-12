# WebSiteManagementClient.AutoHealActions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actionType** | **String** | ActionType - predefined action to be taken | 
**customAction** | [**AutoHealCustomAction**](AutoHealCustomAction.md) |  | [optional] 
**minProcessExecutionTime** | **String** | MinProcessExecutionTime - minimum time the process must execute              before taking the action | [optional] 



## Enum: ActionTypeEnum


* `Recycle` (value: `"Recycle"`)

* `LogEvent` (value: `"LogEvent"`)

* `CustomAction` (value: `"CustomAction"`)




