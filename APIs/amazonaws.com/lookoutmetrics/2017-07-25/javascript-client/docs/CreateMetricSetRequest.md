# AmazonLookoutForMetrics.CreateMetricSetRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**anomalyDetectorArn** | **String** | The ARN of the anomaly detector that will use the dataset. | 
**metricSetName** | **String** | The name of the dataset. | 
**metricSetDescription** | **String** | A description of the dataset you are creating. | [optional] 
**metricList** | [**[Metric]**](Metric.md) | A list of metrics that the dataset will contain. | 
**offset** | **Number** | After an interval ends, the amount of seconds that the detector waits before importing data. Offset is only supported for S3, Redshift, Athena and datasources. | [optional] 
**timestampColumn** | [**CreateMetricSetRequestTimestampColumn**](CreateMetricSetRequestTimestampColumn.md) |  | [optional] 
**dimensionList** | **[String]** | A list of the fields you want to treat as dimensions. | [optional] 
**metricSetFrequency** | **String** | The frequency with which the source data will be analyzed for anomalies. | [optional] 
**metricSource** | [**CreateMetricSetRequestMetricSource**](CreateMetricSetRequestMetricSource.md) |  | 
**timezone** | **String** | The time zone in which your source data was recorded. | [optional] 
**tags** | **{String: String}** | A list of &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lookoutmetrics/latest/dev/detectors-tags.html\&quot;&gt;tags&lt;/a&gt; to apply to the dataset. | [optional] 
**dimensionFilterList** | [**[MetricSetDimensionFilter]**](MetricSetDimensionFilter.md) | A list of filters that specify which data is kept for anomaly detection. | [optional] 



## Enum: MetricSetFrequencyEnum


* `P1D` (value: `"P1D"`)

* `PT1H` (value: `"PT1H"`)

* `PT10M` (value: `"PT10M"`)

* `PT5M` (value: `"PT5M"`)




