

# ProtectedItem

The base class for backup items.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**backupManagementType** | [**BackupManagementTypeEnum**](#BackupManagementTypeEnum) | The backup management type associated with the backup item. |  [optional] |
|**lastRecoveryPoint** | **OffsetDateTime** | The timestamp when the most recent backup copy was created for this backup item. |  [optional] |
|**policyId** | **String** | The ID of the backup policy associated with this backup item. |  [optional] |
|**protectedItemType** | **String** | The backup item type. |  [optional] |
|**sourceResourceId** | **String** | The ID of the resource to be backed up. |  [optional] |
|**workloadType** | [**WorkloadTypeEnum**](#WorkloadTypeEnum) | The workload type for this item. |  [optional] |



## Enum: BackupManagementTypeEnum

| Name | Value |
|---- | -----|
| INVALID | &quot;Invalid&quot; |
| AZURE_IAAS_VM | &quot;AzureIaasVM&quot; |
| MAB | &quot;MAB&quot; |
| DPM | &quot;DPM&quot; |
| AZURE_BACKUP_SERVER | &quot;AzureBackupServer&quot; |
| AZURE_SQL | &quot;AzureSql&quot; |



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
| DPM_UNKNOWN | &quot;DPMUnknown&quot; |



