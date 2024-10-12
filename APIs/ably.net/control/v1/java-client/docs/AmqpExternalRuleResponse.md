

# AmqpExternalRuleResponse


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
|**target** | [**AmqpExternalRulePostTarget**](AmqpExternalRulePostTarget.md) |  |  |
|**version** | **String** |  |  [optional] |



## Enum: RuleTypeEnum

| Name | Value |
|---- | -----|
| AMQP_EXTERNAL | &quot;amqp/external&quot; |



