# GoogleAnalyticsDataApi.Pivot

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fieldNames** | **[String]** | Dimension names for visible columns in the report response. Including \&quot;dateRange\&quot; produces a date range column; for each row in the response, dimension values in the date range column will indicate the corresponding date range from the request. | [optional] 
**limit** | **String** | The number of unique combinations of dimension values to return in this pivot. The &#x60;limit&#x60; parameter is required. A &#x60;limit&#x60; of 10,000 is common for single pivot requests. The product of the &#x60;limit&#x60; for each &#x60;pivot&#x60; in a &#x60;RunPivotReportRequest&#x60; must not exceed 250,000. For example, a two pivot request with &#x60;limit: 1000&#x60; in each pivot will fail because the product is &#x60;1,000,000&#x60;. | [optional] 
**metricAggregations** | **[String]** | Aggregate the metrics by dimensions in this pivot using the specified metric_aggregations. | [optional] 
**offset** | **String** | The row count of the start row. The first row is counted as row 0. | [optional] 
**orderBys** | [**[OrderBy]**](OrderBy.md) | Specifies how dimensions are ordered in the pivot. In the first Pivot, the OrderBys determine Row and PivotDimensionHeader ordering; in subsequent Pivots, the OrderBys determine only PivotDimensionHeader ordering. Dimensions specified in these OrderBys must be a subset of Pivot.field_names. | [optional] 



## Enum: [MetricAggregationsEnum]


* `METRIC_AGGREGATION_UNSPECIFIED` (value: `"METRIC_AGGREGATION_UNSPECIFIED"`)

* `TOTAL` (value: `"TOTAL"`)

* `MINIMUM` (value: `"MINIMUM"`)

* `MAXIMUM` (value: `"MAXIMUM"`)

* `COUNT` (value: `"COUNT"`)




