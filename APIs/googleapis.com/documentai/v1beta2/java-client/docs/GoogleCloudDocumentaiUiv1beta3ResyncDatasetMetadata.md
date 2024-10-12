

# GoogleCloudDocumentaiUiv1beta3ResyncDatasetMetadata

The metadata proto of `ResyncDataset` method.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**commonMetadata** | [**GoogleCloudDocumentaiUiv1beta3CommonOperationMetadata**](GoogleCloudDocumentaiUiv1beta3CommonOperationMetadata.md) |  |  [optional] |
|**datasetResyncStatuses** | [**List&lt;GoogleCloudDocumentaiUiv1beta3ResyncDatasetMetadataDatasetResyncStatus&gt;**](GoogleCloudDocumentaiUiv1beta3ResyncDatasetMetadataDatasetResyncStatus.md) | The list of dataset resync statuses. Not checked when ResyncDatasetRequest.dataset_documents is specified. |  [optional] |
|**individualDocumentResyncStatuses** | [**List&lt;GoogleCloudDocumentaiUiv1beta3ResyncDatasetMetadataIndividualDocumentResyncStatus&gt;**](GoogleCloudDocumentaiUiv1beta3ResyncDatasetMetadataIndividualDocumentResyncStatus.md) | The list of document resync statuses. The same document could have multiple &#x60;individual_document_resync_statuses&#x60; if it has multiple inconsistencies. |  [optional] |



