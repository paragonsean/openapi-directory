# FrontDoorManagementClient.RulesEngineRule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | [**RulesEngineAction**](RulesEngineAction.md) |  | 
**matchConditions** | [**[RulesEngineMatchCondition]**](RulesEngineMatchCondition.md) | A list of match conditions that must meet in order for the actions of this rule to run. Having no match conditions means the actions will always run. | [optional] 
**matchProcessingBehavior** | **String** | If this rule is a match should the rules engine continue running the remaining rules or stop. If not present, defaults to Continue. | [optional] 
**name** | **String** | A name to refer to this specific rule. | 
**priority** | **Number** | A priority assigned to this rule.  | 



## Enum: MatchProcessingBehaviorEnum


* `Continue` (value: `"Continue"`)

* `Stop` (value: `"Stop"`)




