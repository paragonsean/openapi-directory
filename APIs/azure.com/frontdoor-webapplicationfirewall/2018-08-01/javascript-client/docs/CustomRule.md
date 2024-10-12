# WebApplicationFirewallManagement.CustomRule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **String** | Type of Actions | 
**etag** | **String** | Gets a unique read-only string that changes whenever the resource is updated. | [optional] [readonly] 
**matchConditions** | [**[MatchCondition]**](MatchCondition.md) | List of match conditions | 
**name** | **String** | Gets name of the resource that is unique within a policy. This name can be used to access the resource. | [optional] 
**priority** | **Number** | Describes priority of the rule. Rules with a lower value will be evaluated before rules with a higher value | 
**rateLimitDurationInMinutes** | **Number** | Defines rate limit duration. Default - 1 minute | [optional] 
**rateLimitThreshold** | **Number** | Defines rate limit threshold | [optional] 
**ruleType** | **String** | Describes type of rule | 
**transforms** | [**[Transform]**](Transform.md) | List of transforms | [optional] 



## Enum: ActionEnum


* `Allow` (value: `"Allow"`)

* `Block` (value: `"Block"`)

* `Log` (value: `"Log"`)





## Enum: RuleTypeEnum


* `MatchRule` (value: `"MatchRule"`)

* `RateLimitRule` (value: `"RateLimitRule"`)




