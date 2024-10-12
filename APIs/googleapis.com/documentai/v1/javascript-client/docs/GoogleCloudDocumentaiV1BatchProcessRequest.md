# CloudDocumentAiApi.GoogleCloudDocumentaiV1BatchProcessRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**documentOutputConfig** | [**GoogleCloudDocumentaiV1DocumentOutputConfig**](GoogleCloudDocumentaiV1DocumentOutputConfig.md) |  | [optional] 
**inputDocuments** | [**GoogleCloudDocumentaiV1BatchDocumentsInputConfig**](GoogleCloudDocumentaiV1BatchDocumentsInputConfig.md) |  | [optional] 
**labels** | **{String: String}** | Optional. The labels with user-defined metadata for the request. Label keys and values can be no longer than 63 characters (Unicode codepoints) and can only contain lowercase letters, numeric characters, underscores, and dashes. International characters are allowed. Label values are optional. Label keys must start with a letter. | [optional] 
**processOptions** | [**GoogleCloudDocumentaiV1ProcessOptions**](GoogleCloudDocumentaiV1ProcessOptions.md) |  | [optional] 
**skipHumanReview** | **Boolean** | Whether human review should be skipped for this request. Default to &#x60;false&#x60;. | [optional] 


