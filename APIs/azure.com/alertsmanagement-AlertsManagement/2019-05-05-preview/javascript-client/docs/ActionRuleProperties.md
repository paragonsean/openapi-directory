# AzureAlertsManagementServiceResourceProvider.ActionRuleProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditions** | [**Conditions**](Conditions.md) |  | [optional] 
**createdAt** | **Date** | Creation time of action rule. Date-Time in ISO-8601 format. | [optional] [readonly] 
**createdBy** | **String** | Created by user name. | [optional] [readonly] 
**description** | **String** | Description of action rule | [optional] 
**lastModifiedAt** | **Date** | Last updated time of action rule. Date-Time in ISO-8601 format. | [optional] [readonly] 
**lastModifiedBy** | **String** | Last modified by user name. | [optional] [readonly] 
**scope** | [**Scope**](Scope.md) |  | [optional] 
**status** | **String** | Indicates if the given action rule is enabled or disabled | [optional] 
**type** | **String** | Indicates type of action rule | 



## Enum: StatusEnum


* `Enabled` (value: `"Enabled"`)

* `Disabled` (value: `"Disabled"`)





## Enum: TypeEnum


* `Suppression` (value: `"Suppression"`)

* `ActionGroup` (value: `"ActionGroup"`)

* `Diagnostics` (value: `"Diagnostics"`)




