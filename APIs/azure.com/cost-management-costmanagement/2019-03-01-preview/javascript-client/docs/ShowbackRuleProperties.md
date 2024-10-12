# CostManagementClient.ShowbackRuleProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creationTime** | **Date** | The time when the showback rule was created. | [optional] [readonly] 
**deprecationTime** | **Date** | The current time when showback rule was deprecate. | [optional] [readonly] 
**description** | **String** | Description of a showback rule. | [optional] 
**modificationTime** | **Date** | The current status when showback rule was modified. | [optional] [readonly] 
**ruleType** | **String** | The rule type of the showback rule solution. | 
**scopes** | [**[Scope]**](Scope.md) | List of authorized assigned scopes. | [optional] 
**status** | **String** | The current status of the showback rule. | [optional] 
**version** | **Number** | The current version of showback rule. | [optional] [readonly] 



## Enum: RuleTypeEnum


* `CustomPrice` (value: `"CustomPrice"`)

* `CostAllocation` (value: `"CostAllocation"`)





## Enum: StatusEnum


* `NotActive` (value: `"NotActive"`)

* `Active` (value: `"Active"`)




