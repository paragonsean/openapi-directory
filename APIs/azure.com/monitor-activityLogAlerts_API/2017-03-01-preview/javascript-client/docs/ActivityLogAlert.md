# AzureActivityLogAlerts.ActivityLogAlert

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | [**ActivityLogAlertActionList**](ActivityLogAlertActionList.md) |  | 
**condition** | [**ActivityLogAlertAllOfCondition**](ActivityLogAlertAllOfCondition.md) |  | 
**description** | **String** | A description of this activity log alert. | [optional] 
**enabled** | **Boolean** | Indicates whether this activity log alert is enabled. If an activity log alert is not enabled, then none of its actions will be activated. | [optional] [default to true]
**scopes** | **[String]** | A list of resourceIds that will be used as prefixes. The alert will only apply to activityLogs with resourceIds that fall under one of these prefixes. This list must include at least one item. | 


