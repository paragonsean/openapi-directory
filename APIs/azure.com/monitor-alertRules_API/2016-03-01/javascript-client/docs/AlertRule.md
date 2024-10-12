# MonitorManagementClient.AlertRule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | [**[RuleAction]**](RuleAction.md) | the array of actions that are performed when the alert rule becomes active, and when an alert condition is resolved. | [optional] 
**condition** | [**RuleCondition**](RuleCondition.md) |  | 
**description** | **String** | the description of the alert rule that will be included in the alert email. | [optional] 
**isEnabled** | **Boolean** | the flag that indicates whether the alert rule is enabled. | 
**lastUpdatedTime** | **Date** | Last time the rule was updated in ISO8601 format. | [optional] [readonly] 
**name** | **String** | the name of the alert rule. | 


