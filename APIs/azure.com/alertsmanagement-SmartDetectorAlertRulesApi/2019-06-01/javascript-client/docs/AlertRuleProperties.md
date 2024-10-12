# AzureAlertsManagementServiceResourceProvider.AlertRuleProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actionGroups** | [**ActionGroupsInformation**](ActionGroupsInformation.md) |  | 
**description** | **String** | The alert rule description. | [optional] 
**detector** | [**Detector**](Detector.md) |  | 
**frequency** | **String** | The alert rule frequency in ISO8601 format. The time granularity must be in minutes and minimum value is 5 minutes. | 
**scope** | **[String]** | The alert rule resources scope. | 
**severity** | **String** | The alert rule severity. | 
**state** | **String** | The alert rule state. | 
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




