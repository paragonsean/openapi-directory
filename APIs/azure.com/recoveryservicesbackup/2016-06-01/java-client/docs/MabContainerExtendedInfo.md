

# MabContainerExtendedInfo

Additional information for the container.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**backupItemType** | [**BackupItemTypeEnum**](#BackupItemTypeEnum) | The type of backup items associated with this container. |  [optional] |
|**backupItems** | **List&lt;String&gt;** | The list of backup items associated with this container. |  [optional] |
|**lastBackupStatus** | **String** | The latest backup status of this container. |  [optional] |
|**lastRefreshedAt** | **OffsetDateTime** | The time stamp when this container was refreshed. |  [optional] |
|**policyName** | **String** | The backup policy associated with this container. |  [optional] |



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
| DPM_UNKNOWN | &quot;DPMUnknown&quot; |



