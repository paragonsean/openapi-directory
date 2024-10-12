

# MabContainerExtendedInfo

Additional information of the container.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**backupItemType** | [**BackupItemTypeEnum**](#BackupItemTypeEnum) | Type of backup items associated with this container. |  [optional] |
|**backupItems** | **List&lt;String&gt;** | List of backup items associated with this container. |  [optional] |
|**lastBackupStatus** | **String** | Latest backup status of this container. |  [optional] |
|**lastRefreshedAt** | **OffsetDateTime** | Time stamp when this container was refreshed. |  [optional] |
|**policyName** | **String** | Backup policy associated with this container. |  [optional] |



## Enum: BackupItemTypeEnum

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



