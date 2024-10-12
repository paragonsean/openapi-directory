# CloudDocumentAiApi.GoogleCloudDocumentaiV1beta2TableExtractionParams

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **Boolean** | Whether to enable table extraction. | [optional] 
**headerHints** | **[String]** | Optional. Reserved for future use. | [optional] 
**modelVersion** | **String** | Model version of the table extraction system. Default is \&quot;builtin/stable\&quot;. Specify \&quot;builtin/latest\&quot; for the latest model. | [optional] 
**tableBoundHints** | [**[GoogleCloudDocumentaiV1beta2TableBoundHint]**](GoogleCloudDocumentaiV1beta2TableBoundHint.md) | Optional. Table bounding box hints that can be provided to complex cases which our algorithm cannot locate the table(s) in. | [optional] 


