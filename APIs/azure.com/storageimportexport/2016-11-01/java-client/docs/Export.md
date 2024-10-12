

# Export

A property containing information about the blobs to be exported for an export job. This property is required for export jobs, but must not be specified for import jobs.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**blobList** | [**ExportBlobList**](ExportBlobList.md) |  |  [optional] |
|**blobListblobPath** | **String** | The relative URI to the block blob that contains the list of blob paths or blob path prefixes as defined above, beginning with the container name. If the blob is in root container, the URI must begin with $root.  |  [optional] |



