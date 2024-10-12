

# RulesEngineRule

Contains a list of match conditions, and an action on how to modify the request/response. If multiple rules match, the actions from one rule that conflict with a previous rule overwrite for a singular action, or append in the case of headers manipulation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**action** | [**RulesEngineAction**](RulesEngineAction.md) |  |  |
|**matchConditions** | [**List&lt;RulesEngineMatchCondition&gt;**](RulesEngineMatchCondition.md) | A list of match conditions that must meet in order for the actions of this rule to run. Having no match conditions means the actions will always run. |  [optional] |
|**matchProcessingBehavior** | [**MatchProcessingBehaviorEnum**](#MatchProcessingBehaviorEnum) | If this rule is a match should the rules engine continue running the remaining rules or stop. If not present, defaults to Continue. |  [optional] |
|**name** | **String** | A name to refer to this specific rule. |  |
|**priority** | **Integer** | A priority assigned to this rule.  |  |



## Enum: MatchProcessingBehaviorEnum

| Name | Value |
|---- | -----|
| CONTINUE | &quot;Continue&quot; |
| STOP | &quot;Stop&quot; |



