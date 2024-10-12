

# CustomRule

Defines contents of a web application rule

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**action** | [**ActionEnum**](#ActionEnum) | Type of Actions |  |
|**etag** | **String** | Gets a unique read-only string that changes whenever the resource is updated. |  [optional] [readonly] |
|**matchConditions** | [**List&lt;MatchCondition&gt;**](MatchCondition.md) | List of match conditions |  |
|**name** | **String** | Gets name of the resource that is unique within a policy. This name can be used to access the resource. |  [optional] |
|**priority** | **Integer** | Describes priority of the rule. Rules with a lower value will be evaluated before rules with a higher value |  |
|**rateLimitDurationInMinutes** | **Integer** | Defines rate limit duration. Default - 1 minute |  [optional] |
|**rateLimitThreshold** | **Integer** | Defines rate limit threshold |  [optional] |
|**ruleType** | [**RuleTypeEnum**](#RuleTypeEnum) | Describes type of rule |  |
|**transforms** | **List&lt;Transform&gt;** | List of transforms |  [optional] |



## Enum: ActionEnum

| Name | Value |
|---- | -----|
| ALLOW | &quot;Allow&quot; |
| BLOCK | &quot;Block&quot; |
| LOG | &quot;Log&quot; |



## Enum: RuleTypeEnum

| Name | Value |
|---- | -----|
| MATCH_RULE | &quot;MatchRule&quot; |
| RATE_LIMIT_RULE | &quot;RateLimitRule&quot; |



