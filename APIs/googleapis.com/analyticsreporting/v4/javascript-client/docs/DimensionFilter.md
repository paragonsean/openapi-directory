# AnalyticsReportingApi.DimensionFilter

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**caseSensitive** | **Boolean** | Should the match be case sensitive? Default is false. | [optional] 
**dimensionName** | **String** | The dimension to filter on. A DimensionFilter must contain a dimension. | [optional] 
**expressions** | **[String]** | Strings or regular expression to match against. Only the first value of the list is used for comparison unless the operator is &#x60;IN_LIST&#x60;. If &#x60;IN_LIST&#x60; operator, then the entire list is used to filter the dimensions as explained in the description of the &#x60;IN_LIST&#x60; operator. | [optional] 
**not** | **Boolean** | Logical &#x60;NOT&#x60; operator. If this boolean is set to true, then the matching dimension values will be excluded in the report. The default is false. | [optional] 
**operator** | **String** | How to match the dimension to the expression. The default is REGEXP. | [optional] 



## Enum: OperatorEnum


* `OPERATOR_UNSPECIFIED` (value: `"OPERATOR_UNSPECIFIED"`)

* `REGEXP` (value: `"REGEXP"`)

* `BEGINS_WITH` (value: `"BEGINS_WITH"`)

* `ENDS_WITH` (value: `"ENDS_WITH"`)

* `PARTIAL` (value: `"PARTIAL"`)

* `EXACT` (value: `"EXACT"`)

* `NUMERIC_EQUAL` (value: `"NUMERIC_EQUAL"`)

* `NUMERIC_GREATER_THAN` (value: `"NUMERIC_GREATER_THAN"`)

* `NUMERIC_LESS_THAN` (value: `"NUMERIC_LESS_THAN"`)

* `IN_LIST` (value: `"IN_LIST"`)




