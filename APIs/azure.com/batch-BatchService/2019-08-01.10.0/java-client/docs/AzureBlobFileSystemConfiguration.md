

# AzureBlobFileSystemConfiguration


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountKey** | **String** | This property is mutually exclusive with sasKey and one must be specified. |  [optional] |
|**accountName** | **String** |  |  |
|**blobfuseOptions** | **String** | These are &#39;net use&#39; options in Windows and &#39;mount&#39; options in Linux. |  [optional] |
|**containerName** | **String** |  |  |
|**relativeMountPath** | **String** | All file systems are mounted relative to the Batch mounts directory, accessible via the AZ_BATCH_NODE_MOUNTS_DIR environment variable. |  |
|**sasKey** | **String** | This property is mutually exclusive with accountKey and one must be specified. |  [optional] |



