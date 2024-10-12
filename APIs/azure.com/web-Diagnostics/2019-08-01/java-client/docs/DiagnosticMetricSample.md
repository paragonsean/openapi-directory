

# DiagnosticMetricSample

Class representing Diagnostic Metric

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**isAggregated** | **Boolean** | Whether the values are aggregates across all workers or not |  [optional] |
|**maximum** | **Double** | Maximum of the metric sampled during the time period |  [optional] |
|**minimum** | **Double** | Minimum of the metric sampled during the time period |  [optional] |
|**roleInstance** | **String** | Role Instance. Null if this counter is not per instance  This is returned and should be whichever instance name we desire to be returned i.e. CPU and Memory return RDWORKERNAME (LargeDed..._IN_0)  where RDWORKERNAME is Machine name below and RoleInstance name in parenthesis |  [optional] |
|**timestamp** | **OffsetDateTime** | Time at which metric is measured |  [optional] |
|**total** | **Double** | Total value of the metric. If multiple measurements are made this will have sum of all. |  [optional] |



