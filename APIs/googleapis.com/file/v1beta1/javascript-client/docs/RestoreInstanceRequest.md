# CloudFilestoreApi.RestoreInstanceRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fileShare** | **String** | Required. Name of the file share in the Filestore instance that the backup is being restored to. | [optional] 
**sourceBackup** | **String** | The resource name of the backup, in the format &#x60;projects/{project_id}/locations/{location_id}/backups/{backup_id}&#x60;. | [optional] 
**sourceSnapshot** | **String** | The resource name of the snapshot, in the format &#x60;projects/{project_id}/locations/{location_id}/snapshots/{snapshot_id}&#x60;. | [optional] 


