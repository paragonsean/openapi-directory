# CloudDocumentAiApi.GoogleCloudDocumentaiV1beta3DocumentOutputConfigGcsOutputConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fieldMask** | **String** | Specifies which fields to include in the output documents. Only supports top level document and pages field so it must be in the form of &#x60;{document_field_name}&#x60; or &#x60;pages.{page_field_name}&#x60;. | [optional] 
**gcsUri** | **String** | The Cloud Storage uri (a directory) of the output. | [optional] 
**shardingConfig** | [**GoogleCloudDocumentaiV1beta3DocumentOutputConfigGcsOutputConfigShardingConfig**](GoogleCloudDocumentaiV1beta3DocumentOutputConfigGcsOutputConfigShardingConfig.md) |  | [optional] 


