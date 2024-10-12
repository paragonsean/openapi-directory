

# Metric

A message representing the actual monitoring data, values for each key bucket over time, of a metric.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**aggregation** | [**AggregationEnum**](#AggregationEnum) | The aggregation function used to aggregate each key bucket |  [optional] |
|**category** | [**LocalizedString**](LocalizedString.md) |  |  [optional] |
|**derived** | [**DerivedMetric**](DerivedMetric.md) |  |  [optional] |
|**displayLabel** | [**LocalizedString**](LocalizedString.md) |  |  [optional] |
|**hasNonzeroData** | **Boolean** | Whether the metric has any non-zero data. |  [optional] |
|**hotValue** | **Float** | The value that is considered hot for the metric. On a per metric basis hotness signals high utilization and something that might potentially be a cause for concern by the end user. hot_value is used to calibrate and scale visual color scales. |  [optional] |
|**indexedHotKeys** | [**Map&lt;String, IndexedHotKey&gt;**](IndexedHotKey.md) | The (sparse) mapping from time index to an IndexedHotKey message, representing those time intervals for which there are hot keys. |  [optional] |
|**indexedKeyRangeInfos** | [**Map&lt;String, IndexedKeyRangeInfos&gt;**](IndexedKeyRangeInfos.md) | The (sparse) mapping from time interval index to an IndexedKeyRangeInfos message, representing those time intervals for which there are informational messages concerning key ranges. |  [optional] |
|**info** | [**LocalizedString**](LocalizedString.md) |  |  [optional] |
|**matrix** | [**MetricMatrix**](MetricMatrix.md) |  |  [optional] |
|**unit** | [**LocalizedString**](LocalizedString.md) |  |  [optional] |
|**visible** | **Boolean** | Whether the metric is visible to the end user. |  [optional] |



## Enum: AggregationEnum

| Name | Value |
|---- | -----|
| AGGREGATION_UNSPECIFIED | &quot;AGGREGATION_UNSPECIFIED&quot; |
| MAX | &quot;MAX&quot; |
| SUM | &quot;SUM&quot; |



