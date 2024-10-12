

# GoogleCloudDocumentaiV1beta3BatchProcessMetadataIndividualProcessStatus

The status of a each individual document in the batch process.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**humanReviewOperation** | **String** | The name of the operation triggered by the processed document. If the human review process isn&#39;t triggered, this field will be empty. It has the same response type and metadata as the long-running operation returned by the ReviewDocument method. |  [optional] |
|**humanReviewStatus** | [**GoogleCloudDocumentaiV1beta3HumanReviewStatus**](GoogleCloudDocumentaiV1beta3HumanReviewStatus.md) |  |  [optional] |
|**inputGcsSource** | **String** | The source of the document, same as the input_gcs_source field in the request when the batch process started. |  [optional] |
|**outputGcsDestination** | **String** | The Cloud Storage output destination (in the request as DocumentOutputConfig.GcsOutputConfig.gcs_uri) of the processed document if it was successful, otherwise empty. |  [optional] |
|**status** | [**GoogleRpcStatus**](GoogleRpcStatus.md) |  |  [optional] |



