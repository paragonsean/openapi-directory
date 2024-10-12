

# StorageProfile

Storage Profile properties of a server

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**backupRetentionDays** | **Integer** | Backup retention days for the server. |  [optional] |
|**geoRedundantBackup** | [**GeoRedundantBackupEnum**](#GeoRedundantBackupEnum) | Enable Geo-redundant or not for server backup. |  [optional] |
|**storageAutogrow** | [**StorageAutogrowEnum**](#StorageAutogrowEnum) | Enable Storage Auto Grow. |  [optional] |
|**storageMB** | **Integer** | Max storage allowed for a server. |  [optional] |



## Enum: GeoRedundantBackupEnum

| Name | Value |
|---- | -----|
| ENABLED | &quot;Enabled&quot; |
| DISABLED | &quot;Disabled&quot; |



## Enum: StorageAutogrowEnum

| Name | Value |
|---- | -----|
| ENABLED | &quot;Enabled&quot; |
| DISABLED | &quot;Disabled&quot; |



