

# IntelligenceCloudAutomlXpsMetricEntry


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**argentumMetricId** | **String** | For billing metrics that are using legacy sku&#39;s, set the legacy billing metric id here. This will be sent to Chemist as the \&quot;cloudbilling.googleapis.com/argentum_metric_id\&quot; label. Otherwise leave empty. |  [optional] |
|**doubleValue** | **Double** | A double value. |  [optional] |
|**int64Value** | **String** | A signed 64-bit integer value. |  [optional] |
|**metricName** | **String** | The metric name defined in the service configuration. |  [optional] |
|**systemLabels** | [**List&lt;IntelligenceCloudAutomlXpsMetricEntryLabel&gt;**](IntelligenceCloudAutomlXpsMetricEntryLabel.md) | Billing system labels for this (metric, value) pair. |  [optional] |



