

# CustomRule

Defines contents of a web application rule

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**action** | **ActionType** |  |  |
|**enabledState** | [**EnabledStateEnum**](#EnabledStateEnum) | Describes if the custom rule is in enabled or disabled state. Defaults to Enabled if not specified. |  [optional] |
|**matchConditions** | [**List&lt;MatchCondition&gt;**](MatchCondition.md) | List of match conditions. |  |
|**name** | **String** | Describes the name of the rule. |  [optional] |
|**priority** | **Integer** | Describes priority of the rule. Rules with a lower value will be evaluated before rules with a higher value. |  |
|**rateLimitDurationInMinutes** | **Integer** | Time window for resetting the rate limit count. Default is 1 minute. |  [optional] |
|**rateLimitThreshold** | **Integer** | Number of allowed requests per client within the time window. |  [optional] |
|**ruleType** | [**RuleTypeEnum**](#RuleTypeEnum) | Describes type of rule. |  |



## Enum: EnabledStateEnum

| Name | Value |
|---- | -----|
| DISABLED | &quot;Disabled&quot; |
| ENABLED | &quot;Enabled&quot; |



## Enum: RuleTypeEnum

| Name | Value |
|---- | -----|
| MATCH_RULE | &quot;MatchRule&quot; |
| RATE_LIMIT_RULE | &quot;RateLimitRule&quot; |



