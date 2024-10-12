

# GoogleCloudDiscoveryengineV1alphaSearchResponseSummary

Summary of the top N search result specified by the summary spec.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**safetyAttributes** | [**GoogleCloudDiscoveryengineV1alphaSearchResponseSummarySafetyAttributes**](GoogleCloudDiscoveryengineV1alphaSearchResponseSummarySafetyAttributes.md) |  |  [optional] |
|**summarySkippedReasons** | [**List&lt;SummarySkippedReasonsEnum&gt;**](#List&lt;SummarySkippedReasonsEnum&gt;) | Additional summary-skipped reasons. This provides the reason for ignored cases. If nothing is skipped, this field is not set. |  [optional] |
|**summaryText** | **String** | The summary content. |  [optional] |
|**summaryWithMetadata** | [**GoogleCloudDiscoveryengineV1alphaSearchResponseSummarySummaryWithMetadata**](GoogleCloudDiscoveryengineV1alphaSearchResponseSummarySummaryWithMetadata.md) |  |  [optional] |



## Enum: List&lt;SummarySkippedReasonsEnum&gt;

| Name | Value |
|---- | -----|
| SUMMARY_SKIPPED_REASON_UNSPECIFIED | &quot;SUMMARY_SKIPPED_REASON_UNSPECIFIED&quot; |
| ADVERSARIAL_QUERY_IGNORED | &quot;ADVERSARIAL_QUERY_IGNORED&quot; |
| NON_SUMMARY_SEEKING_QUERY_IGNORED | &quot;NON_SUMMARY_SEEKING_QUERY_IGNORED&quot; |
| OUT_OF_DOMAIN_QUERY_IGNORED | &quot;OUT_OF_DOMAIN_QUERY_IGNORED&quot; |
| POTENTIAL_POLICY_VIOLATION | &quot;POTENTIAL_POLICY_VIOLATION&quot; |
| LLM_ADDON_NOT_ENABLED | &quot;LLM_ADDON_NOT_ENABLED&quot; |



