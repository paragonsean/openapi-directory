

# GoogleCloudVisionV1p4beta1InputConfig

The desired input location and metadata.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**content** | **byte[]** | File content, represented as a stream of bytes. Note: As with all &#x60;bytes&#x60; fields, protobuffers use a pure binary representation, whereas JSON representations use base64. Currently, this field only works for BatchAnnotateFiles requests. It does not work for AsyncBatchAnnotateFiles requests. |  [optional] |
|**gcsSource** | [**GoogleCloudVisionV1p4beta1GcsSource**](GoogleCloudVisionV1p4beta1GcsSource.md) |  |  [optional] |
|**mimeType** | **String** | The type of the file. Currently only \&quot;application/pdf\&quot;, \&quot;image/tiff\&quot; and \&quot;image/gif\&quot; are supported. Wildcards are not supported. |  [optional] |



