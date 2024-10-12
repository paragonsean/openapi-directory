# CloudFilestoreApi.FileShareConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capacityGb** | **String** | File share capacity in gigabytes (GB). Filestore defines 1 GB as 1024^3 bytes. | [optional] 
**name** | **String** | Required. The name of the file share. Must use 1-16 characters for the basic service tier and 1-63 characters for all other service tiers. Must use lowercase letters, numbers, or underscores &#x60;[a-z0-9_]&#x60;. Must start with a letter. Immutable. | [optional] 
**nfsExportOptions** | [**[NfsExportOptions]**](NfsExportOptions.md) | Nfs Export Options. There is a limit of 10 export options per file share. | [optional] 
**sourceBackup** | **String** | The resource name of the backup, in the format &#x60;projects/{project_number}/locations/{location_id}/backups/{backup_id}&#x60;, that this file share has been restored from. | [optional] 


