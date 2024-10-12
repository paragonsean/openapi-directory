

# GoogleCloudDocumentaiV1beta3ImportDocumentsMetadata

Metadata of the import document operation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**commonMetadata** | [**GoogleCloudDocumentaiV1beta3CommonOperationMetadata**](GoogleCloudDocumentaiV1beta3CommonOperationMetadata.md) |  |  [optional] |
|**importConfigValidationResults** | [**List&lt;GoogleCloudDocumentaiV1beta3ImportDocumentsMetadataImportConfigValidationResult&gt;**](GoogleCloudDocumentaiV1beta3ImportDocumentsMetadataImportConfigValidationResult.md) | Validation statuses of the batch documents import config. |  [optional] |
|**individualImportStatuses** | [**List&lt;GoogleCloudDocumentaiV1beta3ImportDocumentsMetadataIndividualImportStatus&gt;**](GoogleCloudDocumentaiV1beta3ImportDocumentsMetadataIndividualImportStatus.md) | The list of response details of each document. |  [optional] |
|**totalDocumentCount** | **Integer** | Total number of the documents that are qualified for importing. |  [optional] |



