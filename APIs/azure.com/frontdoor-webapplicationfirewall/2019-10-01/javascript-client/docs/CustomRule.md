# WebApplicationFirewallManagement.CustomRule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | [**ActionType**](ActionType.md) |  | 
**enabledState** | **String** | Describes if the custom rule is in enabled or disabled state. Defaults to Enabled if not specified. | [optional] 
**matchConditions** | [**[MatchCondition]**](MatchCondition.md) | List of match conditions. | 
**name** | **String** | Describes the name of the rule. | [optional] 
**priority** | **Number** | Describes priority of the rule. Rules with a lower value will be evaluated before rules with a higher value. | 
**rateLimitDurationInMinutes** | **Number** | Time window for resetting the rate limit count. Default is 1 minute. | [optional] 
**rateLimitThreshold** | **Number** | Number of allowed requests per client within the time window. | [optional] 
**ruleType** | **String** | Describes type of rule. | 



## Enum: EnabledStateEnum


* `Disabled` (value: `"Disabled"`)

* `Enabled` (value: `"Enabled"`)





## Enum: RuleTypeEnum


* `MatchRule` (value: `"MatchRule"`)

* `RateLimitRule` (value: `"RateLimitRule"`)




