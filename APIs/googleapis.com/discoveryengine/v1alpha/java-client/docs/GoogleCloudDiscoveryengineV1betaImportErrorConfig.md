

# GoogleCloudDiscoveryengineV1betaImportErrorConfig

Configuration of destination for Import related errors.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**gcsPrefix** | **String** | Cloud Storage prefix for import errors. This must be an empty, existing Cloud Storage directory. Import errors are written to sharded files in this directory, one per line, as a JSON-encoded &#x60;google.rpc.Status&#x60; message. |  [optional] |



