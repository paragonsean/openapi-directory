

# GoogleCloudDocumentaiV1beta3BatchProcessRequest

Request message for BatchProcessDocuments.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**documentOutputConfig** | [**GoogleCloudDocumentaiV1beta3DocumentOutputConfig**](GoogleCloudDocumentaiV1beta3DocumentOutputConfig.md) |  |  [optional] |
|**inputConfigs** | [**List&lt;GoogleCloudDocumentaiV1beta3BatchProcessRequestBatchInputConfig&gt;**](GoogleCloudDocumentaiV1beta3BatchProcessRequestBatchInputConfig.md) | The input config for each single document in the batch process. |  [optional] |
|**inputDocuments** | [**GoogleCloudDocumentaiV1beta3BatchDocumentsInputConfig**](GoogleCloudDocumentaiV1beta3BatchDocumentsInputConfig.md) |  |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | Optional. The labels with user-defined metadata for the request. Label keys and values can be no longer than 63 characters (Unicode codepoints) and can only contain lowercase letters, numeric characters, underscores, and dashes. International characters are allowed. Label values are optional. Label keys must start with a letter. |  [optional] |
|**outputConfig** | [**GoogleCloudDocumentaiV1beta3BatchProcessRequestBatchOutputConfig**](GoogleCloudDocumentaiV1beta3BatchProcessRequestBatchOutputConfig.md) |  |  [optional] |
|**processOptions** | [**GoogleCloudDocumentaiV1beta3ProcessOptions**](GoogleCloudDocumentaiV1beta3ProcessOptions.md) |  |  [optional] |
|**skipHumanReview** | **Boolean** | Whether human review should be skipped for this request. Default to &#x60;false&#x60;. |  [optional] |



