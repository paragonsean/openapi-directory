# AnalyticsReportingApi.MetricFilterClause

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | [**[MetricFilter]**](MetricFilter.md) | The repeated set of filters. They are logically combined based on the operator specified. | [optional] 
**operator** | **String** | The operator for combining multiple metric filters. If unspecified, it is treated as an &#x60;OR&#x60;. | [optional] 



## Enum: OperatorEnum


* `OPERATOR_UNSPECIFIED` (value: `"OPERATOR_UNSPECIFIED"`)

* `OR` (value: `"OR"`)

* `AND` (value: `"AND"`)




