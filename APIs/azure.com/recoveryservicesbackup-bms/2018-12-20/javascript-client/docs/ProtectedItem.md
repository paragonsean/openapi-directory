# RecoveryServicesBackupClient.ProtectedItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backupManagementType** | **String** | Type of backup management for the backed up item. | [optional] 
**backupSetName** | **String** | Name of the backup set the backup item belongs to | [optional] 
**containerName** | **String** | Unique name of container | [optional] 
**createMode** | **String** | Create mode to indicate recovery of existing soft deleted data source or creation of new data source. | [optional] 
**deferredDeleteTimeInUTC** | **Date** | Time for deferred deletion in UTC | [optional] 
**deferredDeleteTimeRemaining** | **String** | Time remaining before the DS marked for deferred delete is permanently deleted | [optional] 
**isDeferredDeleteScheduleUpcoming** | **Boolean** | Flag to identify whether the deferred deleted DS is to be purged soon | [optional] 
**isRehydrate** | **Boolean** | Flag to identify that deferred deleted DS is to be moved into Pause state | [optional] 
**isScheduledForDeferredDelete** | **Boolean** | Flag to identify whether the DS is scheduled for deferred delete | [optional] 
**lastRecoveryPoint** | **Date** | Timestamp when the last (latest) backup copy was created for this backup item. | [optional] 
**policyId** | **String** | ID of the backup policy with which this item is backed up. | [optional] 
**protectedItemType** | **String** | backup item type. | 
**sourceResourceId** | **String** | ARM ID of the resource to be backed up. | [optional] 
**workloadType** | **String** | Type of workload this item represents. | [optional] 



## Enum: BackupManagementTypeEnum


* `Invalid` (value: `"Invalid"`)

* `AzureIaasVM` (value: `"AzureIaasVM"`)

* `MAB` (value: `"MAB"`)

* `DPM` (value: `"DPM"`)

* `AzureBackupServer` (value: `"AzureBackupServer"`)

* `AzureSql` (value: `"AzureSql"`)

* `AzureStorage` (value: `"AzureStorage"`)

* `AzureWorkload` (value: `"AzureWorkload"`)

* `DefaultBackup` (value: `"DefaultBackup"`)





## Enum: CreateModeEnum


* `Invalid` (value: `"Invalid"`)

* `Default` (value: `"Default"`)

* `Recover` (value: `"Recover"`)





## Enum: WorkloadTypeEnum


* `Invalid` (value: `"Invalid"`)

* `VM` (value: `"VM"`)

* `FileFolder` (value: `"FileFolder"`)

* `AzureSqlDb` (value: `"AzureSqlDb"`)

* `SQLDB` (value: `"SQLDB"`)

* `Exchange` (value: `"Exchange"`)

* `Sharepoint` (value: `"Sharepoint"`)

* `VMwareVM` (value: `"VMwareVM"`)

* `SystemState` (value: `"SystemState"`)

* `Client` (value: `"Client"`)

* `GenericDataSource` (value: `"GenericDataSource"`)

* `SQLDataBase` (value: `"SQLDataBase"`)

* `AzureFileShare` (value: `"AzureFileShare"`)

* `SAPHanaDatabase` (value: `"SAPHanaDatabase"`)

* `SAPAseDatabase` (value: `"SAPAseDatabase"`)




