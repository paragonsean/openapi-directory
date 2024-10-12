# CloudMonitoringApi.Aggregation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alignmentPeriod** | **String** | The alignment_period specifies a time interval, in seconds, that is used to divide the data in all the time series into consistent blocks of time. This will be done before the per-series aligner can be applied to the data.The value must be at least 60 seconds. If a per-series aligner other than ALIGN_NONE is specified, this field is required or an error is returned. If no per-series aligner is specified, or the aligner ALIGN_NONE is specified, then this field is ignored.The maximum value of the alignment_period is 2 years, or 104 weeks. | [optional] 
**crossSeriesReducer** | **String** | The reduction operation to be used to combine time series into a single time series, where the value of each data point in the resulting series is a function of all the already aligned values in the input time series.Not all reducer operations can be applied to all time series. The valid choices depend on the metric_kind and the value_type of the original time series. Reduction can yield a time series with a different metric_kind or value_type than the input time series.Time series data must first be aligned (see per_series_aligner) in order to perform cross-time series reduction. If cross_series_reducer is specified, then per_series_aligner must be specified, and must not be ALIGN_NONE. An alignment_period must also be specified; otherwise, an error is returned. | [optional] 
**groupByFields** | **[String]** | The set of fields to preserve when cross_series_reducer is specified. The group_by_fields determine how the time series are partitioned into subsets prior to applying the aggregation operation. Each subset contains time series that have the same value for each of the grouping fields. Each individual time series is a member of exactly one subset. The cross_series_reducer is applied to each subset of time series. It is not possible to reduce across different resource types, so this field implicitly contains resource.type. Fields not specified in group_by_fields are aggregated away. If group_by_fields is not specified and all the time series have the same resource type, then the time series are aggregated into a single output time series. If cross_series_reducer is not defined, this field is ignored. | [optional] 
**perSeriesAligner** | **String** | An Aligner describes how to bring the data points in a single time series into temporal alignment. Except for ALIGN_NONE, all alignments cause all the data points in an alignment_period to be mathematically grouped together, resulting in a single data point for each alignment_period with end timestamp at the end of the period.Not all alignment operations may be applied to all time series. The valid choices depend on the metric_kind and value_type of the original time series. Alignment can change the metric_kind or the value_type of the time series.Time series data must be aligned in order to perform cross-time series reduction. If cross_series_reducer is specified, then per_series_aligner must be specified and not equal to ALIGN_NONE and alignment_period must be specified; otherwise, an error is returned. | [optional] 



## Enum: CrossSeriesReducerEnum


* `NONE` (value: `"REDUCE_NONE"`)

* `MEAN` (value: `"REDUCE_MEAN"`)

* `MIN` (value: `"REDUCE_MIN"`)

* `MAX` (value: `"REDUCE_MAX"`)

* `SUM` (value: `"REDUCE_SUM"`)

* `STDDEV` (value: `"REDUCE_STDDEV"`)

* `COUNT` (value: `"REDUCE_COUNT"`)

* `COUNT_TRUE` (value: `"REDUCE_COUNT_TRUE"`)

* `COUNT_FALSE` (value: `"REDUCE_COUNT_FALSE"`)

* `FRACTION_TRUE` (value: `"REDUCE_FRACTION_TRUE"`)

* `PERCENTILE_99` (value: `"REDUCE_PERCENTILE_99"`)

* `PERCENTILE_95` (value: `"REDUCE_PERCENTILE_95"`)

* `PERCENTILE_50` (value: `"REDUCE_PERCENTILE_50"`)

* `PERCENTILE_05` (value: `"REDUCE_PERCENTILE_05"`)





## Enum: PerSeriesAlignerEnum


* `NONE` (value: `"ALIGN_NONE"`)

* `DELTA` (value: `"ALIGN_DELTA"`)

* `RATE` (value: `"ALIGN_RATE"`)

* `INTERPOLATE` (value: `"ALIGN_INTERPOLATE"`)

* `NEXT_OLDER` (value: `"ALIGN_NEXT_OLDER"`)

* `MIN` (value: `"ALIGN_MIN"`)

* `MAX` (value: `"ALIGN_MAX"`)

* `MEAN` (value: `"ALIGN_MEAN"`)

* `COUNT` (value: `"ALIGN_COUNT"`)

* `SUM` (value: `"ALIGN_SUM"`)

* `STDDEV` (value: `"ALIGN_STDDEV"`)

* `COUNT_TRUE` (value: `"ALIGN_COUNT_TRUE"`)

* `COUNT_FALSE` (value: `"ALIGN_COUNT_FALSE"`)

* `FRACTION_TRUE` (value: `"ALIGN_FRACTION_TRUE"`)

* `PERCENTILE_99` (value: `"ALIGN_PERCENTILE_99"`)

* `PERCENTILE_95` (value: `"ALIGN_PERCENTILE_95"`)

* `PERCENTILE_50` (value: `"ALIGN_PERCENTILE_50"`)

* `PERCENTILE_05` (value: `"ALIGN_PERCENTILE_05"`)

* `PERCENT_CHANGE` (value: `"ALIGN_PERCENT_CHANGE"`)




