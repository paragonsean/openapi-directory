

# OrderBy

Order bys define how rows will be sorted in the response. For example, ordering rows by descending event count is one ordering, and ordering rows by the event name string is a different ordering.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**desc** | **Boolean** | If true, sorts by descending order. |  [optional] |
|**dimension** | [**DimensionOrderBy**](DimensionOrderBy.md) |  |  [optional] |
|**metric** | [**MetricOrderBy**](MetricOrderBy.md) |  |  [optional] |
|**pivot** | [**PivotOrderBy**](PivotOrderBy.md) |  |  [optional] |



