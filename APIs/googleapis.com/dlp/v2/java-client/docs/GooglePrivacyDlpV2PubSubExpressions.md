

# GooglePrivacyDlpV2PubSubExpressions

An expression, consisting of an operator and conditions.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**conditions** | [**List&lt;GooglePrivacyDlpV2PubSubCondition&gt;**](GooglePrivacyDlpV2PubSubCondition.md) | Conditions to apply to the expression. |  [optional] |
|**logicalOperator** | [**LogicalOperatorEnum**](#LogicalOperatorEnum) | The operator to apply to the collection of conditions. |  [optional] |



## Enum: LogicalOperatorEnum

| Name | Value |
|---- | -----|
| LOGICAL_OPERATOR_UNSPECIFIED | &quot;LOGICAL_OPERATOR_UNSPECIFIED&quot; |
| OR | &quot;OR&quot; |
| AND | &quot;AND&quot; |



