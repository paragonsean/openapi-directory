

# GoogleCloudContactcenterinsightsV1alpha1IngestConversationsMetadataIngestConversationsStats

Statistics for IngestConversations operation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**duplicatesSkippedCount** | **Integer** | Output only. The number of objects skipped because another conversation with the same transcript uri had already been ingested. |  [optional] [readonly] |
|**failedIngestCount** | **Integer** | Output only. The number of objects which were unable to be ingested due to errors. The errors are populated in the partial_errors field. |  [optional] [readonly] |
|**processedObjectCount** | **Integer** | Output only. The number of objects processed during the ingest operation. |  [optional] [readonly] |
|**successfulIngestCount** | **Integer** | Output only. The number of new conversations added during this ingest operation. |  [optional] [readonly] |



