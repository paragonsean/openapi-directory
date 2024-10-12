

# ResourceFile

A file to be downloaded from Azure blob storage to a compute node.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**blobSource** | **String** | Gets or sets the URL of a blob in Azure storage. The Batch service downloads the blob to the specified file path. The URL must be readable using anonymous access. |  [optional] |
|**filePath** | **String** | Gets or sets the location on the compute node to which the file should be downloaded. |  [optional] |



