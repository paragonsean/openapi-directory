# VertexAiApi.GoogleCloudAiplatformV1NfsMount

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mountPoint** | **String** | Required. Destination mount path. The NFS will be mounted for the user under /mnt/nfs/ | [optional] 
**path** | **String** | Required. Source path exported from NFS server. Has to start with &#39;/&#39;, and combined with the ip address, it indicates the source mount path in the form of &#x60;server:path&#x60; | [optional] 
**server** | **String** | Required. IP address of the NFS server. | [optional] 


