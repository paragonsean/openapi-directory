# ConsumptionManagementClient.Notification

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contactEmails** | **[String]** | Email addresses to send the budget notification to when the threshold is exceeded. | 
**contactGroups** | **[String]** | Action groups to send the budget notification to when the threshold is exceeded. | [optional] 
**contactRoles** | **[String]** | Contact roles to send the budget notification to when the threshold is exceeded. | [optional] 
**enabled** | **Boolean** | The notification is enabled or not. | 
**operator** | **String** | The comparison operator. | 
**threshold** | **Number** | Threshold value associated with a notification. Notification is sent when the cost exceeded the threshold. It is always percent and has to be between 0 and 1000. | 



## Enum: OperatorEnum


* `EqualTo` (value: `"EqualTo"`)

* `GreaterThan` (value: `"GreaterThan"`)

* `GreaterThanOrEqualTo` (value: `"GreaterThanOrEqualTo"`)




