

# PivotOrderBy

Sorts by a pivot column group.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**metricName** | **String** | In the response to order by, order rows by this column. Must be a metric name from the request. |  [optional] |
|**pivotSelections** | [**List&lt;PivotSelection&gt;**](PivotSelection.md) | Used to select a dimension name and value pivot. If multiple pivot selections are given, the sort occurs on rows where all pivot selection dimension name and value pairs match the row&#39;s dimension name and value pair. |  [optional] |



