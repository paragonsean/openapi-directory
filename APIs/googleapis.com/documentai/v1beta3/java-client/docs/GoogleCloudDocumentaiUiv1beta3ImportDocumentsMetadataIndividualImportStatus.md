

# GoogleCloudDocumentaiUiv1beta3ImportDocumentsMetadataIndividualImportStatus

The status of each individual document in the import process.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**inputGcsSource** | **String** | The source Cloud Storage URI of the document. |  [optional] |
|**outputDocumentId** | [**GoogleCloudDocumentaiUiv1beta3DocumentId**](GoogleCloudDocumentaiUiv1beta3DocumentId.md) |  |  [optional] |
|**outputGcsDestination** | **String** | The output_gcs_destination of the processed document if it was successful, otherwise empty. |  [optional] |
|**status** | [**GoogleRpcStatus**](GoogleRpcStatus.md) |  |  [optional] |



