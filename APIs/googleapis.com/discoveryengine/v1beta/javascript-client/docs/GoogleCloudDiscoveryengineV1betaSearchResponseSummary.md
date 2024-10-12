# DiscoveryEngineApi.GoogleCloudDiscoveryengineV1betaSearchResponseSummary

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**safetyAttributes** | [**GoogleCloudDiscoveryengineV1betaSearchResponseSummarySafetyAttributes**](GoogleCloudDiscoveryengineV1betaSearchResponseSummarySafetyAttributes.md) |  | [optional] 
**summarySkippedReasons** | **[String]** | Additional summary-skipped reasons. This provides the reason for ignored cases. If nothing is skipped, this field is not set. | [optional] 
**summaryText** | **String** | The summary content. | [optional] 
**summaryWithMetadata** | [**GoogleCloudDiscoveryengineV1betaSearchResponseSummarySummaryWithMetadata**](GoogleCloudDiscoveryengineV1betaSearchResponseSummarySummaryWithMetadata.md) |  | [optional] 



## Enum: [SummarySkippedReasonsEnum]


* `SUMMARY_SKIPPED_REASON_UNSPECIFIED` (value: `"SUMMARY_SKIPPED_REASON_UNSPECIFIED"`)

* `ADVERSARIAL_QUERY_IGNORED` (value: `"ADVERSARIAL_QUERY_IGNORED"`)

* `NON_SUMMARY_SEEKING_QUERY_IGNORED` (value: `"NON_SUMMARY_SEEKING_QUERY_IGNORED"`)

* `OUT_OF_DOMAIN_QUERY_IGNORED` (value: `"OUT_OF_DOMAIN_QUERY_IGNORED"`)

* `POTENTIAL_POLICY_VIOLATION` (value: `"POTENTIAL_POLICY_VIOLATION"`)

* `LLM_ADDON_NOT_ENABLED` (value: `"LLM_ADDON_NOT_ENABLED"`)




