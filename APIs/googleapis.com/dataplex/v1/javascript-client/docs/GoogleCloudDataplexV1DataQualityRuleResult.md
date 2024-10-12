# CloudDataplexApi.GoogleCloudDataplexV1DataQualityRuleResult

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**evaluatedCount** | **String** | The number of rows a rule was evaluated against.This field is only valid for row-level type rules.Evaluated count can be configured to either include all rows (default) - with null rows automatically failing rule evaluation, or exclude null rows from the evaluated_count, by setting ignore_nulls &#x3D; true. | [optional] 
**failingRowsQuery** | **String** | The query to find rows that did not pass this rule.This field is only valid for row-level type rules. | [optional] 
**nullCount** | **String** | The number of rows with null values in the specified column. | [optional] 
**passRatio** | **Number** | The ratio of passed_count / evaluated_count.This field is only valid for row-level type rules. | [optional] 
**passed** | **Boolean** | Whether the rule passed or failed. | [optional] 
**passedCount** | **String** | The number of rows which passed a rule evaluation.This field is only valid for row-level type rules. | [optional] 
**rule** | [**GoogleCloudDataplexV1DataQualityRule**](GoogleCloudDataplexV1DataQualityRule.md) |  | [optional] 


