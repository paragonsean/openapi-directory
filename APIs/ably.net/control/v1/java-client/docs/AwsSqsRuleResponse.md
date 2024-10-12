

# AwsSqsRuleResponse


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
|**target** | [**AwsSqsRuleResponseTarget**](AwsSqsRuleResponseTarget.md) |  |  |
|**version** | **String** |  |  [optional] |



## Enum: RuleTypeEnum

| Name | Value |
|---- | -----|
| AWS_SQS | &quot;aws/sqs&quot; |



