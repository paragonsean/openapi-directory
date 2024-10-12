

# ProtectionIntent

Base class for backup ProtectionIntent.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**backupManagementType** | [**BackupManagementTypeEnum**](#BackupManagementTypeEnum) | Type of backup management for the backed up item. |  [optional] |
|**itemId** | **String** | ID of the item which is getting protected, In case of Azure Vm , it is ProtectedItemId |  [optional] |
|**policyId** | **String** | ID of the backup policy with which this item is backed up. |  [optional] |
|**protectionIntentItemType** | **String** | backup protectionIntent type. |  [optional] |
|**protectionState** | [**ProtectionStateEnum**](#ProtectionStateEnum) | Backup state of this backup item. |  [optional] |
|**sourceResourceId** | **String** | ARM ID of the resource to be backed up. |  [optional] |



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



## Enum: ProtectionStateEnum

| Name | Value |
|---- | -----|
| INVALID | &quot;Invalid&quot; |
| NOT_PROTECTED | &quot;NotProtected&quot; |
| PROTECTING | &quot;Protecting&quot; |
| PROTECTED | &quot;Protected&quot; |
| PROTECTION_FAILED | &quot;ProtectionFailed&quot; |



