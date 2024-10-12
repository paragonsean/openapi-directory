

# RestoreInstanceRequest

RestoreInstanceRequest restores an existing instance's file share from a backup.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**fileShare** | **String** | Required. Name of the file share in the Filestore instance that the backup is being restored to. |  [optional] |
|**sourceBackup** | **String** | The resource name of the backup, in the format &#x60;projects/{project_number}/locations/{location_id}/backups/{backup_id}&#x60;. |  [optional] |



