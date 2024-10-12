

# ShowbackRuleProperties

The properties of a showback rule.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**creationTime** | **OffsetDateTime** | The time when the showback rule was created. |  [optional] [readonly] |
|**deprecationTime** | **OffsetDateTime** | The current time when showback rule was deprecate. |  [optional] [readonly] |
|**description** | **String** | Description of a showback rule. |  [optional] |
|**modificationTime** | **OffsetDateTime** | The current status when showback rule was modified. |  [optional] [readonly] |
|**ruleType** | [**RuleTypeEnum**](#RuleTypeEnum) | The rule type of the showback rule solution. |  |
|**scopes** | [**List&lt;Scope&gt;**](Scope.md) | List of authorized assigned scopes. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The current status of the showback rule. |  [optional] |
|**version** | **Integer** | The current version of showback rule. |  [optional] [readonly] |



## Enum: RuleTypeEnum

| Name | Value |
|---- | -----|
| CUSTOM_PRICE | &quot;CustomPrice&quot; |
| COST_ALLOCATION | &quot;CostAllocation&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| NOT_ACTIVE | &quot;NotActive&quot; |
| ACTIVE | &quot;Active&quot; |



