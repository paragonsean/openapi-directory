

# GoogleCloudRetailV2alphaExportErrorsConfig

Configuration of destination for Export related errors.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**gcsPrefix** | **String** | Google Cloud Storage path for import errors. This must be an empty, existing Cloud Storage bucket. Export errors will be written to a file in this bucket, one per line, as a JSON-encoded &#x60;google.rpc.Status&#x60; message. |  [optional] |



