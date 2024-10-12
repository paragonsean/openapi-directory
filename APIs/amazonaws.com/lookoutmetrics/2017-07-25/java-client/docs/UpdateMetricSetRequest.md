

# UpdateMetricSetRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**metricSetArn** | **String** | The ARN of the dataset to update. |  |
|**metricSetDescription** | **String** | The dataset&#39;s description. |  [optional] |
|**metricList** | [**List&lt;Metric&gt;**](Metric.md) | The metric list. |  [optional] |
|**offset** | **Integer** | After an interval ends, the amount of seconds that the detector waits before importing data. Offset is only supported for S3, Redshift, Athena and datasources. |  [optional] |
|**timestampColumn** | [**CreateMetricSetRequestTimestampColumn**](CreateMetricSetRequestTimestampColumn.md) |  |  [optional] |
|**dimensionList** | **List&lt;String&gt;** | The dimension list. |  [optional] |
|**metricSetFrequency** | [**MetricSetFrequencyEnum**](#MetricSetFrequencyEnum) | The dataset&#39;s interval. |  [optional] |
|**metricSource** | [**CreateMetricSetRequestMetricSource**](CreateMetricSetRequestMetricSource.md) |  |  [optional] |
|**dimensionFilterList** | [**List&lt;MetricSetDimensionFilter&gt;**](MetricSetDimensionFilter.md) | Describes a list of filters for choosing specific dimensions and specific values. Each filter consists of the dimension and one of its values that you want to include. When multiple dimensions or values are specified, the dimensions are joined with an AND operation and the values are joined with an OR operation. |  [optional] |



## Enum: MetricSetFrequencyEnum

| Name | Value |
|---- | -----|
| P1_D | &quot;P1D&quot; |
| PT1_H | &quot;PT1H&quot; |
| PT10_M | &quot;PT10M&quot; |
| PT5_M | &quot;PT5M&quot; |



