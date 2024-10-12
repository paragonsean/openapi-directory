# AzureAlertsManagementServiceResourceProvider.AlertRulePatchProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actionGroups** | [**ActionGroupsInformation**](ActionGroupsInformation.md) |  | [optional] 
**description** | **String** | The alert rule description. | [optional] 
**frequency** | **String** | The alert rule frequency in ISO8601 format. The time granularity must be in minutes and minimum value is 5 minutes. | [optional] 
**severity** | **String** | The alert rule severity. | [optional] 
**state** | **String** | The alert rule state. | [optional] 
**throttling** | [**ThrottlingInformation**](ThrottlingInformation.md) |  | [optional] 



## Enum: SeverityEnum


* `Sev0` (value: `"Sev0"`)

* `Sev1` (value: `"Sev1"`)

* `Sev2` (value: `"Sev2"`)

* `Sev3` (value: `"Sev3"`)

* `Sev4` (value: `"Sev4"`)





## Enum: StateEnum


* `Enabled` (value: `"Enabled"`)

* `Disabled` (value: `"Disabled"`)




