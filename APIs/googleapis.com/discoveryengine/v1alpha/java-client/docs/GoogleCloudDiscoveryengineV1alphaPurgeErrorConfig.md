

# GoogleCloudDiscoveryengineV1alphaPurgeErrorConfig

Configuration of destination for Purge related errors.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**gcsPrefix** | **String** | Cloud Storage prefix for purge errors. This must be an empty, existing Cloud Storage directory. Purge errors are written to sharded files in this directory, one per line, as a JSON-encoded &#x60;google.rpc.Status&#x60; message. |  [optional] |



