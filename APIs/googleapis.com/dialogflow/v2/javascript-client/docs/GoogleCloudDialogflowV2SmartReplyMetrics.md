# DialogflowApi.GoogleCloudDialogflowV2SmartReplyMetrics

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowlistCoverage** | **Number** | Percentage of target participant messages in the evaluation dataset for which similar messages have appeared at least once in the allowlist. Should be [0, 1]. | [optional] 
**conversationCount** | **String** | Total number of conversations used to generate this metric. | [optional] 
**topNMetrics** | [**[GoogleCloudDialogflowV2SmartReplyMetricsTopNMetrics]**](GoogleCloudDialogflowV2SmartReplyMetricsTopNMetrics.md) | Metrics of top n smart replies, sorted by TopNMetric.n. | [optional] 


