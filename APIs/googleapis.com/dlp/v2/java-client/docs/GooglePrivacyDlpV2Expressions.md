

# GooglePrivacyDlpV2Expressions

An expression, consisting of an operator and conditions.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**conditions** | [**GooglePrivacyDlpV2Conditions**](GooglePrivacyDlpV2Conditions.md) |  |  [optional] |
|**logicalOperator** | [**LogicalOperatorEnum**](#LogicalOperatorEnum) | The operator to apply to the result of conditions. Default and currently only supported value is &#x60;AND&#x60;. |  [optional] |



## Enum: LogicalOperatorEnum

| Name | Value |
|---- | -----|
| LOGICAL_OPERATOR_UNSPECIFIED | &quot;LOGICAL_OPERATOR_UNSPECIFIED&quot; |
| AND | &quot;AND&quot; |



