

# ResourceFile

A file to be downloaded from Azure blob storage to a compute node.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**blobSource** | **String** | The URL of the file within Azure Blob Storage. This URL should include a shared access signature if the blob is not publicly readable. |  [optional] |
|**fileMode** | **String** | The file mode attribute in octal format. This property will be ignored if it is specified for a resourceFile which will be downloaded to a Windows compute node. |  [optional] |
|**filePath** | **String** | The location to which to download the file, relative to the task&#39;s working directory. |  [optional] |



