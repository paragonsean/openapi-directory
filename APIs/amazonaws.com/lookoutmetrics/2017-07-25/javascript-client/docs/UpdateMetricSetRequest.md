# AmazonLookoutForMetrics.UpdateMetricSetRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metricSetArn** | **String** | The ARN of the dataset to update. | 
**metricSetDescription** | **String** | The dataset&#39;s description. | [optional] 
**metricList** | [**[Metric]**](Metric.md) | The metric list. | [optional] 
**offset** | **Number** | After an interval ends, the amount of seconds that the detector waits before importing data. Offset is only supported for S3, Redshift, Athena and datasources. | [optional] 
**timestampColumn** | [**CreateMetricSetRequestTimestampColumn**](CreateMetricSetRequestTimestampColumn.md) |  | [optional] 
**dimensionList** | **[String]** | The dimension list. | [optional] 
**metricSetFrequency** | **String** | The dataset&#39;s interval. | [optional] 
**metricSource** | [**CreateMetricSetRequestMetricSource**](CreateMetricSetRequestMetricSource.md) |  | [optional] 
**dimensionFilterList** | [**[MetricSetDimensionFilter]**](MetricSetDimensionFilter.md) | Describes a list of filters for choosing specific dimensions and specific values. Each filter consists of the dimension and one of its values that you want to include. When multiple dimensions or values are specified, the dimensions are joined with an AND operation and the values are joined with an OR operation. | [optional] 



## Enum: MetricSetFrequencyEnum


* `P1D` (value: `"P1D"`)

* `PT1H` (value: `"PT1H"`)

* `PT10M` (value: `"PT10M"`)

* `PT5M` (value: `"PT5M"`)




