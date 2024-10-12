

# AlgorithmRulesSignalComparison

A single comparison. The comparison compares the `signal` to the `comparisonValue`. The comparison of `siteId==123` is represented with the following field values: * `signal` has an `impressionSignal` of `SITE_ID`. * `comparisonOperator` is set to `EQUAL`. * `comparisonValue` is set to 123.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**comparisonOperator** | [**ComparisonOperatorEnum**](#ComparisonOperatorEnum) | Operator used to compare the two values. In the resulting experession, the &#x60;signal&#x60; will be the first value and the &#x60;comparisonValue will be the second. |  [optional] |
|**comparisonValue** | [**AlgorithmRulesComparisonValue**](AlgorithmRulesComparisonValue.md) |  |  [optional] |
|**signal** | [**AlgorithmRulesSignal**](AlgorithmRulesSignal.md) |  |  [optional] |



## Enum: ComparisonOperatorEnum

| Name | Value |
|---- | -----|
| COMPARISON_OPERATOR_UNSPECIFIED | &quot;COMPARISON_OPERATOR_UNSPECIFIED&quot; |
| EQUAL | &quot;EQUAL&quot; |
| GREATER_THAN | &quot;GREATER_THAN&quot; |
| LESS_THAN | &quot;LESS_THAN&quot; |
| GREATER_THAN_OR_EQUAL_TO | &quot;GREATER_THAN_OR_EQUAL_TO&quot; |
| LESS_THAN_OR_EQUAL_TO | &quot;LESS_THAN_OR_EQUAL_TO&quot; |



