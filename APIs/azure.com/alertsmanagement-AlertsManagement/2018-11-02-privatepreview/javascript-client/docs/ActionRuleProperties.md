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
**resourceGroup** | **String** | Resource group where action rule is stored | [optional] [readonly] 
**scope** | [**Scope**](Scope.md) |  | [optional] 
**status** | **String** | Indicates if the given action rule is enabled or disabled | [optional] 
**suppressionConfig** | [**SuppressionConfig**](SuppressionConfig.md) |  | [optional] 



## Enum: StatusEnum


* `enabled` (value: `"enabled"`)

* `disabled` (value: `"disabled"`)




