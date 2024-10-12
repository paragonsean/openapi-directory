

# ProtectedItem

Base class for backup items.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**backupManagementType** | [**BackupManagementTypeEnum**](#BackupManagementTypeEnum) | Type of backup management for the backed up item. |  [optional] |
|**backupSetName** | **String** | Name of the backup set the backup item belongs to |  [optional] |
|**containerName** | **String** | Unique name of container |  [optional] |
|**createMode** | [**CreateModeEnum**](#CreateModeEnum) | Create mode to indicate recovery of existing soft deleted data source or creation of new data source. |  [optional] |
|**deferredDeleteTimeInUTC** | **OffsetDateTime** | Time for deferred deletion in UTC |  [optional] |
|**deferredDeleteTimeRemaining** | **String** | Time remaining before the DS marked for deferred delete is permanently deleted |  [optional] |
|**isDeferredDeleteScheduleUpcoming** | **Boolean** | Flag to identify whether the deferred deleted DS is to be purged soon |  [optional] |
|**isRehydrate** | **Boolean** | Flag to identify that deferred deleted DS is to be moved into Pause state |  [optional] |
|**isScheduledForDeferredDelete** | **Boolean** | Flag to identify whether the DS is scheduled for deferred delete |  [optional] |
|**lastRecoveryPoint** | **OffsetDateTime** | Timestamp when the last (latest) backup copy was created for this backup item. |  [optional] |
|**policyId** | **String** | ID of the backup policy with which this item is backed up. |  [optional] |
|**protectedItemType** | **String** | backup item type. |  |
|**sourceResourceId** | **String** | ARM ID of the resource to be backed up. |  [optional] |
|**workloadType** | [**WorkloadTypeEnum**](#WorkloadTypeEnum) | Type of workload this item represents. |  [optional] |



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



## Enum: CreateModeEnum

| Name | Value |
|---- | -----|
| INVALID | &quot;Invalid&quot; |
| DEFAULT | &quot;Default&quot; |
| RECOVER | &quot;Recover&quot; |



## Enum: WorkloadTypeEnum

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



