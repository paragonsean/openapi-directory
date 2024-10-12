# AnalyticsReportingApi.SegmentDimensionFilter

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**caseSensitive** | **Boolean** | Should the match be case sensitive, ignored for &#x60;IN_LIST&#x60; operator. | [optional] 
**dimensionName** | **String** | Name of the dimension for which the filter is being applied. | [optional] 
**expressions** | **[String]** | The list of expressions, only the first element is used for all operators | [optional] 
**maxComparisonValue** | **String** | Maximum comparison values for &#x60;BETWEEN&#x60; match type. | [optional] 
**minComparisonValue** | **String** | Minimum comparison values for &#x60;BETWEEN&#x60; match type. | [optional] 
**operator** | **String** | The operator to use to match the dimension with the expressions. | [optional] 



## Enum: OperatorEnum


* `OPERATOR_UNSPECIFIED` (value: `"OPERATOR_UNSPECIFIED"`)

* `REGEXP` (value: `"REGEXP"`)

* `BEGINS_WITH` (value: `"BEGINS_WITH"`)

* `ENDS_WITH` (value: `"ENDS_WITH"`)

* `PARTIAL` (value: `"PARTIAL"`)

* `EXACT` (value: `"EXACT"`)

* `IN_LIST` (value: `"IN_LIST"`)

* `NUMERIC_LESS_THAN` (value: `"NUMERIC_LESS_THAN"`)

* `NUMERIC_GREATER_THAN` (value: `"NUMERIC_GREATER_THAN"`)

* `NUMERIC_BETWEEN` (value: `"NUMERIC_BETWEEN"`)




