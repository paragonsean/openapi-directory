

# BMSWorkloadItemQueryObject

Filters to list items that can be backed up.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**backupManagementType** | [**BackupManagementTypeEnum**](#BackupManagementTypeEnum) | Backup management type. |  [optional] |
|**protectionStatus** | [**ProtectionStatusEnum**](#ProtectionStatusEnum) | Backup status query parameter. |  [optional] |
|**workloadItemType** | [**WorkloadItemTypeEnum**](#WorkloadItemTypeEnum) | Workload Item type |  [optional] |
|**workloadType** | [**WorkloadTypeEnum**](#WorkloadTypeEnum) | Workload type |  [optional] |



## Enum: BackupManagementTypeEnum

| Name | Value |
|---- | -----|
| INVALID | &quot;Invalid&quot; |
| AZURE_IAAS_VM | &quot;AzureIaasVM&quot; |
| MAB | &quot;MAB&quot; |
| DPM | &quot;DPM&quot; |
| AZURE_SQL | &quot;AzureSql&quot; |
| AZURE_BACKUP_SERVER | &quot;AzureBackupServer&quot; |
| AZURE_WORKLOAD | &quot;AzureWorkload&quot; |
| AZURE_STORAGE | &quot;AzureStorage&quot; |
| DEFAULT_BACKUP | &quot;DefaultBackup&quot; |



## Enum: ProtectionStatusEnum

| Name | Value |
|---- | -----|
| INVALID | &quot;Invalid&quot; |
| NOT_PROTECTED | &quot;NotProtected&quot; |
| PROTECTING | &quot;Protecting&quot; |
| PROTECTED | &quot;Protected&quot; |
| PROTECTION_FAILED | &quot;ProtectionFailed&quot; |



## Enum: WorkloadItemTypeEnum

| Name | Value |
|---- | -----|
| INVALID | &quot;Invalid&quot; |
| SQL_INSTANCE | &quot;SQLInstance&quot; |
| SQL_DATA_BASE | &quot;SQLDataBase&quot; |
| SAP_HANA_SYSTEM | &quot;SAPHanaSystem&quot; |
| SAP_HANA_DATABASE | &quot;SAPHanaDatabase&quot; |
| SAP_ASE_SYSTEM | &quot;SAPAseSystem&quot; |
| SAP_ASE_DATABASE | &quot;SAPAseDatabase&quot; |



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



