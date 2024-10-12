

# AlgorithmRulesRuleset

A ruleset consisting of a list of rules and how to aggregate the resulting values.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**aggregationType** | [**AggregationTypeEnum**](#AggregationTypeEnum) | How to aggregate values of evaluated rules. |  [optional] |
|**maxValue** | **Double** | Maximum value the ruleset can evaluate to. |  [optional] |
|**rules** | [**List&lt;AlgorithmRulesRule&gt;**](AlgorithmRulesRule.md) | List of rules to generate the impression value. |  [optional] |



## Enum: AggregationTypeEnum

| Name | Value |
|---- | -----|
| RULE_AGGREGATION_TYPE_UNSPECIFIED | &quot;RULE_AGGREGATION_TYPE_UNSPECIFIED&quot; |
| SUM_OF_VALUES | &quot;SUM_OF_VALUES&quot; |
| PRODUCT_OF_VALUES | &quot;PRODUCT_OF_VALUES&quot; |
| MAXIMUM_VALUE | &quot;MAXIMUM_VALUE&quot; |



