# ContactCenterAiInsightsApi.GoogleCloudContactcenterinsightsV1alpha1IngestConversationsMetadataIngestConversationsStats

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**duplicatesSkippedCount** | **Number** | Output only. The number of objects skipped because another conversation with the same transcript uri had already been ingested. | [optional] [readonly] 
**failedIngestCount** | **Number** | Output only. The number of objects which were unable to be ingested due to errors. The errors are populated in the partial_errors field. | [optional] [readonly] 
**processedObjectCount** | **Number** | Output only. The number of objects processed during the ingest operation. | [optional] [readonly] 
**successfulIngestCount** | **Number** | Output only. The number of new conversations added during this ingest operation. | [optional] [readonly] 


