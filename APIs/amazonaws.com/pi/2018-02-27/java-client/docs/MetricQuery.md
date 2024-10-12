

# MetricQuery

A single query to be processed. You must provide the metric to query. If no other parameters are specified, Performance Insights returns all data points for the specified metric. Optionally, you can request that the data points be aggregated by dimension group (<code>GroupBy</code>), and return only those data points that match your criteria (<code>Filter</code>).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**metric** | [**String**](String.md) |  |  |
|**groupBy** | [**MetricQueryGroupBy**](MetricQueryGroupBy.md) |  |  [optional] |
|**filter** | [**Map**](Map.md) |  |  [optional] |



