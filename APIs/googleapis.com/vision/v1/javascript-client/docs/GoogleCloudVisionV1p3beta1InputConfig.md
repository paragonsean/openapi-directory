# CloudVisionApi.GoogleCloudVisionV1p3beta1InputConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **Blob** | File content, represented as a stream of bytes. Note: As with all &#x60;bytes&#x60; fields, protobuffers use a pure binary representation, whereas JSON representations use base64. Currently, this field only works for BatchAnnotateFiles requests. It does not work for AsyncBatchAnnotateFiles requests. | [optional] 
**gcsSource** | [**GoogleCloudVisionV1p3beta1GcsSource**](GoogleCloudVisionV1p3beta1GcsSource.md) |  | [optional] 
**mimeType** | **String** | The type of the file. Currently only \&quot;application/pdf\&quot;, \&quot;image/tiff\&quot; and \&quot;image/gif\&quot; are supported. Wildcards are not supported. | [optional] 


