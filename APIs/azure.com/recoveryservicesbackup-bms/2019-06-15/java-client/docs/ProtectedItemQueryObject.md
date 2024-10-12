

# ProtectedItemQueryObject

Filters to list backup items.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**backupEngineName** | **String** | Backup Engine name |  [optional] |
|**backupManagementType** | [**BackupManagementTypeEnum**](#BackupManagementTypeEnum) | Backup management type for the backed up item. |  [optional] |
|**backupSetName** | **String** | Name of the backup set. |  [optional] |
|**containerName** | **String** | Name of the container. |  [optional] |
|**fabricName** | **String** | Name of the fabric. |  [optional] |
|**friendlyName** | **String** | Friendly name of protected item |  [optional] |
|**healthState** | [**HealthStateEnum**](#HealthStateEnum) | Health State for the backed up item. |  [optional] |
|**itemType** | [**ItemTypeEnum**](#ItemTypeEnum) | Type of workload this item represents. |  [optional] |
|**policyName** | **String** | Backup policy name associated with the backup item. |  [optional] |



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



## Enum: HealthStateEnum

| Name | Value |
|---- | -----|
| PASSED | &quot;Passed&quot; |
| ACTION_REQUIRED | &quot;ActionRequired&quot; |
| ACTION_SUGGESTED | &quot;ActionSuggested&quot; |
| INVALID | &quot;Invalid&quot; |



## Enum: ItemTypeEnum

| Name | Value |
|---- | -----|
| INVALID | &quot;Invalid&quot; |
| VM | &quot;VM&quot; |
| FILE_FOLDER | &quot;FileFolder&quot; |
| AZURE_SQL_DB | &quot;AzureSqlDb&quot; |
| SQLDB | &quot;SQLDB&quot; |
| EXCHANGE | &quot;Exchange&quot; |
| SHAREPOINT | &quot;Sharepoint&quot; |
| V_MWARE_VM | &quot;VMwareVM&quot; |
| SYSTEM_STATE | &quot;SystemState&quot; |
| CLIENT | &quot;Client&quot; |
| GENERIC_DATA_SOURCE | &quot;GenericDataSource&quot; |
| SQL_DATA_BASE | &quot;SQLDataBase&quot; |
| AZURE_FILE_SHARE | &quot;AzureFileShare&quot; |
| SAP_HANA_DATABASE | &quot;SAPHanaDatabase&quot; |
| SAP_ASE_DATABASE | &quot;SAPAseDatabase&quot; |



