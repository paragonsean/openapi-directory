# PostgreSqlManagementClient.StorageProfile

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backupRetentionDays** | **Number** | Backup retention days for the server. | [optional] 
**geoRedundantBackup** | **String** | Enable Geo-redundant or not for server backup. | [optional] 
**storageAutogrow** | **String** | Enable Storage Auto Grow. | [optional] 
**storageMB** | **Number** | Max storage allowed for a server. | [optional] 



## Enum: GeoRedundantBackupEnum


* `Enabled` (value: `"Enabled"`)

* `Disabled` (value: `"Disabled"`)





## Enum: StorageAutogrowEnum


* `Enabled` (value: `"Enabled"`)

* `Disabled` (value: `"Disabled"`)




