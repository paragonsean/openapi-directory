# CloudDocumentAiApi.GoogleCloudDocumentaiV1beta2InputConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contents** | **Blob** | Content in bytes, represented as a stream of bytes. Note: As with all &#x60;bytes&#x60; fields, proto buffer messages use a pure binary representation, whereas JSON representations use base64. This field only works for synchronous ProcessDocument method. | [optional] 
**gcsSource** | [**GoogleCloudDocumentaiV1beta2GcsSource**](GoogleCloudDocumentaiV1beta2GcsSource.md) |  | [optional] 
**mimeType** | **String** | Required. Mimetype of the input. Current supported mimetypes are application/pdf, image/tiff, and image/gif. In addition, application/json type is supported for requests with ProcessDocumentRequest.automl_params field set. The JSON file needs to be in Document format. | [optional] 


