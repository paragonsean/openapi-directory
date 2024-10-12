

# PerStepNamespaceMetrics

Metrics for a particular unfused step and namespace. A metric is uniquely identified by the `metrics_namespace`, `original_step`, `metric name` and `metric_labels`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**metricValues** | [**List&lt;MetricValue&gt;**](MetricValue.md) | Optional. Metrics that are recorded for this namespace and unfused step. |  [optional] |
|**metricsNamespace** | **String** | The namespace of these metrics on the worker. |  [optional] |
|**originalStep** | **String** | The original system name of the unfused step that these metrics are reported from. |  [optional] |



