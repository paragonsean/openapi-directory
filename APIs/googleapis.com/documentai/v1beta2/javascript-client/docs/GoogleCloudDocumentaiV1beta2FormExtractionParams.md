# CloudDocumentAiApi.GoogleCloudDocumentaiV1beta2FormExtractionParams

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **Boolean** | Whether to enable form extraction. | [optional] 
**keyValuePairHints** | [**[GoogleCloudDocumentaiV1beta2KeyValuePairHint]**](GoogleCloudDocumentaiV1beta2KeyValuePairHint.md) | Reserved for future use. | [optional] 
**modelVersion** | **String** | Model version of the form extraction system. Default is \&quot;builtin/stable\&quot;. Specify \&quot;builtin/latest\&quot; for the latest model. For custom form models, specify: \&quot;custom/{model_name}\&quot;. Model name format is \&quot;bucket_name/path/to/modeldir\&quot; corresponding to \&quot;gs://bucket_name/path/to/modeldir\&quot; where annotated examples are stored. | [optional] 


