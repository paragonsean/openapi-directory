# RecoveryServicesBackupClient.ProtectedItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backupManagementType** | **String** | The backup management type associated with the backup item. | [optional] 
**lastRecoveryPoint** | **Date** | The timestamp when the most recent backup copy was created for this backup item. | [optional] 
**policyId** | **String** | The ID of the backup policy associated with this backup item. | [optional] 
**protectedItemType** | **String** | The backup item type. | [optional] 
**sourceResourceId** | **String** | The ID of the resource to be backed up. | [optional] 
**workloadType** | **String** | The workload type for this item. | [optional] 



## Enum: BackupManagementTypeEnum


* `Invalid` (value: `"Invalid"`)

* `AzureIaasVM` (value: `"AzureIaasVM"`)

* `MAB` (value: `"MAB"`)

* `DPM` (value: `"DPM"`)

* `AzureBackupServer` (value: `"AzureBackupServer"`)

* `AzureSql` (value: `"AzureSql"`)





## Enum: WorkloadTypeEnum


* `Invalid` (value: `"Invalid"`)

* `VM` (value: `"VM"`)

* `FileFolder` (value: `"FileFolder"`)

* `AzureSqlDb` (value: `"AzureSqlDb"`)

* `SQLDB` (value: `"SQLDB"`)

* `Exchange` (value: `"Exchange"`)

* `Sharepoint` (value: `"Sharepoint"`)

* `DPMUnknown` (value: `"DPMUnknown"`)




