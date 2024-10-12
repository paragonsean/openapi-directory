

# GoogleCloudDocumentaiV1beta1InputConfig

The desired input location and metadata.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**gcsSource** | [**GoogleCloudDocumentaiV1beta1GcsSource**](GoogleCloudDocumentaiV1beta1GcsSource.md) |  |  [optional] |
|**mimeType** | **String** | Required. Mimetype of the input. Current supported mimetypes are application/pdf, image/tiff, and image/gif. In addition, application/json type is supported for requests with ProcessDocumentRequest.automl_params field set. The JSON file needs to be in Document format. |  [optional] |



