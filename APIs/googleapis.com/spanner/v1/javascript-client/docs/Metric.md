# CloudSpannerApi.Metric

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregation** | **String** | The aggregation function used to aggregate each key bucket | [optional] 
**category** | [**LocalizedString**](LocalizedString.md) |  | [optional] 
**derived** | [**DerivedMetric**](DerivedMetric.md) |  | [optional] 
**displayLabel** | [**LocalizedString**](LocalizedString.md) |  | [optional] 
**hasNonzeroData** | **Boolean** | Whether the metric has any non-zero data. | [optional] 
**hotValue** | **Number** | The value that is considered hot for the metric. On a per metric basis hotness signals high utilization and something that might potentially be a cause for concern by the end user. hot_value is used to calibrate and scale visual color scales. | [optional] 
**indexedHotKeys** | [**{String: IndexedHotKey}**](IndexedHotKey.md) | The (sparse) mapping from time index to an IndexedHotKey message, representing those time intervals for which there are hot keys. | [optional] 
**indexedKeyRangeInfos** | [**{String: IndexedKeyRangeInfos}**](IndexedKeyRangeInfos.md) | The (sparse) mapping from time interval index to an IndexedKeyRangeInfos message, representing those time intervals for which there are informational messages concerning key ranges. | [optional] 
**info** | [**LocalizedString**](LocalizedString.md) |  | [optional] 
**matrix** | [**MetricMatrix**](MetricMatrix.md) |  | [optional] 
**unit** | [**LocalizedString**](LocalizedString.md) |  | [optional] 
**visible** | **Boolean** | Whether the metric is visible to the end user. | [optional] 



## Enum: AggregationEnum


* `AGGREGATION_UNSPECIFIED` (value: `"AGGREGATION_UNSPECIFIED"`)

* `MAX` (value: `"MAX"`)

* `SUM` (value: `"SUM"`)




