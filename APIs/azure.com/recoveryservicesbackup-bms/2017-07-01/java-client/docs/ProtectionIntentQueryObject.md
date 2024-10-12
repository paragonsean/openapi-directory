

# ProtectionIntentQueryObject

Filters to list protection intent.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**backupManagementType** | [**BackupManagementTypeEnum**](#BackupManagementTypeEnum) | Backup management type for the backed up item |  [optional] |
|**itemName** | **String** | Item name of the intent |  [optional] |
|**itemType** | [**ItemTypeEnum**](#ItemTypeEnum) | Type of workload this item represents |  [optional] |
|**parentName** | **String** | Parent name of the intent |  [optional] |



## Enum: BackupManagementTypeEnum

| Name | Value |
|---- | -----|
| INVALID | &quot;Invalid&quot; |
| AZURE_IAAS_VM | &quot;AzureIaasVM&quot; |
| MAB | &quot;MAB&quot; |
| DPM | &quot;DPM&quot; |
| AZURE_BACKUP_SERVER | &quot;AzureBackupServer&quot; |
| AZURE_SQL | &quot;AzureSql&quot; |
| AZURE_STORAGE | &quot;AzureStorage&quot; |
| AZURE_WORKLOAD | &quot;AzureWorkload&quot; |
| DEFAULT_BACKUP | &quot;DefaultBackup&quot; |



## Enum: ItemTypeEnum

| Name | Value |
|---- | -----|
| INVALID | &quot;Invalid&quot; |
| SQL_INSTANCE | &quot;SQLInstance&quot; |
| SQL_AVAILABILITY_GROUP_CONTAINER | &quot;SQLAvailabilityGroupContainer&quot; |



