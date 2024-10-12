

# ZapierRuleResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**links** | **Object** |  |  [optional] |
|**appId** | **String** |  |  [optional] |
|**created** | **BigDecimal** |  |  [optional] |
|**id** | **String** |  |  [optional] |
|**modified** | **BigDecimal** |  |  [optional] |
|**requestMode** | **String** |  |  |
|**ruleType** | [**RuleTypeEnum**](#RuleTypeEnum) |  |  |
|**source** | [**RuleSource**](RuleSource.md) |  |  |
|**status** | **String** |  |  [optional] |
|**target** | [**CloudflareWorkerRulePostTarget**](CloudflareWorkerRulePostTarget.md) |  |  |
|**version** | **String** |  |  [optional] |



## Enum: RuleTypeEnum

| Name | Value |
|---- | -----|
| HTTP_ZAPIER | &quot;http/zapier&quot; |



