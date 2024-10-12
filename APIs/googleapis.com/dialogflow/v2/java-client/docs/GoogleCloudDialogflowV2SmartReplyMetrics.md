

# GoogleCloudDialogflowV2SmartReplyMetrics

The evaluation metrics for smart reply model.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowlistCoverage** | **Float** | Percentage of target participant messages in the evaluation dataset for which similar messages have appeared at least once in the allowlist. Should be [0, 1]. |  [optional] |
|**conversationCount** | **String** | Total number of conversations used to generate this metric. |  [optional] |
|**topNMetrics** | [**List&lt;GoogleCloudDialogflowV2SmartReplyMetricsTopNMetrics&gt;**](GoogleCloudDialogflowV2SmartReplyMetricsTopNMetrics.md) | Metrics of top n smart replies, sorted by TopNMetric.n. |  [optional] |



