

# GoogleCloudDocumentaiV1BatchProcessMetadataIndividualProcessStatus

The status of a each individual document in the batch process.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**humanReviewStatus** | [**GoogleCloudDocumentaiV1HumanReviewStatus**](GoogleCloudDocumentaiV1HumanReviewStatus.md) |  |  [optional] |
|**inputGcsSource** | **String** | The source of the document, same as the input_gcs_source field in the request when the batch process started. |  [optional] |
|**outputGcsDestination** | **String** | The Cloud Storage output destination (in the request as DocumentOutputConfig.GcsOutputConfig.gcs_uri) of the processed document if it was successful, otherwise empty. |  [optional] |
|**status** | [**GoogleRpcStatus**](GoogleRpcStatus.md) |  |  [optional] |



