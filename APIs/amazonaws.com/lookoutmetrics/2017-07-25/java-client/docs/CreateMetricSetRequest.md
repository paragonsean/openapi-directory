

# CreateMetricSetRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**anomalyDetectorArn** | **String** | The ARN of the anomaly detector that will use the dataset. |  |
|**metricSetName** | **String** | The name of the dataset. |  |
|**metricSetDescription** | **String** | A description of the dataset you are creating. |  [optional] |
|**metricList** | [**List&lt;Metric&gt;**](Metric.md) | A list of metrics that the dataset will contain. |  |
|**offset** | **Integer** | After an interval ends, the amount of seconds that the detector waits before importing data. Offset is only supported for S3, Redshift, Athena and datasources. |  [optional] |
|**timestampColumn** | [**CreateMetricSetRequestTimestampColumn**](CreateMetricSetRequestTimestampColumn.md) |  |  [optional] |
|**dimensionList** | **List&lt;String&gt;** | A list of the fields you want to treat as dimensions. |  [optional] |
|**metricSetFrequency** | [**MetricSetFrequencyEnum**](#MetricSetFrequencyEnum) | The frequency with which the source data will be analyzed for anomalies. |  [optional] |
|**metricSource** | [**CreateMetricSetRequestMetricSource**](CreateMetricSetRequestMetricSource.md) |  |  |
|**timezone** | **String** | The time zone in which your source data was recorded. |  [optional] |
|**tags** | **Map&lt;String, String&gt;** | A list of &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lookoutmetrics/latest/dev/detectors-tags.html\&quot;&gt;tags&lt;/a&gt; to apply to the dataset. |  [optional] |
|**dimensionFilterList** | [**List&lt;MetricSetDimensionFilter&gt;**](MetricSetDimensionFilter.md) | A list of filters that specify which data is kept for anomaly detection. |  [optional] |



## Enum: MetricSetFrequencyEnum

| Name | Value |
|---- | -----|
| P1_D | &quot;P1D&quot; |
| PT1_H | &quot;PT1H&quot; |
| PT10_M | &quot;PT10M&quot; |
| PT5_M | &quot;PT5M&quot; |



