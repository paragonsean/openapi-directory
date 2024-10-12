# DisplayVideo360Api.AlgorithmRulesRuleset

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregationType** | **String** | How to aggregate values of evaluated rules. | [optional] 
**maxValue** | **Number** | Maximum value the ruleset can evaluate to. | [optional] 
**rules** | [**[AlgorithmRulesRule]**](AlgorithmRulesRule.md) | List of rules to generate the impression value. | [optional] 



## Enum: AggregationTypeEnum


* `RULE_AGGREGATION_TYPE_UNSPECIFIED` (value: `"RULE_AGGREGATION_TYPE_UNSPECIFIED"`)

* `SUM_OF_VALUES` (value: `"SUM_OF_VALUES"`)

* `PRODUCT_OF_VALUES` (value: `"PRODUCT_OF_VALUES"`)

* `MAXIMUM_VALUE` (value: `"MAXIMUM_VALUE"`)




