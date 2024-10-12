# BatchService.AzureFileShareConfiguration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountKey** | **String** |  | 
**accountName** | **String** |  | 
**azureFileUrl** | **String** | This is of the form &#39;https://{account}.file.core.windows.net/&#39;. | 
**mountOptions** | **String** | These are &#39;net use&#39; options in Windows and &#39;mount&#39; options in Linux. | [optional] 
**relativeMountPath** | **String** | All file systems are mounted relative to the Batch mounts directory, accessible via the AZ_BATCH_NODE_MOUNTS_DIR environment variable. | 


