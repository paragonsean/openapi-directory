# AlloyDbApi.RestoreClusterRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backupSource** | [**BackupSource**](BackupSource.md) |  | [optional] 
**cluster** | [**Cluster**](Cluster.md) |  | [optional] 
**clusterId** | **String** | Required. ID of the requesting object. | [optional] 
**continuousBackupSource** | [**ContinuousBackupSource**](ContinuousBackupSource.md) |  | [optional] 
**requestId** | **String** | Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). | [optional] 
**validateOnly** | **Boolean** | Optional. If set, performs request validation (e.g. permission checks and any other type of validation), but do not actually execute the import request. | [optional] 


