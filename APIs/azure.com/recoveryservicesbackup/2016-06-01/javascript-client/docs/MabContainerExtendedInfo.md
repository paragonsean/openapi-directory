# RecoveryServicesBackupClient.MabContainerExtendedInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backupItemType** | **String** | The type of backup items associated with this container. | [optional] 
**backupItems** | **[String]** | The list of backup items associated with this container. | [optional] 
**lastBackupStatus** | **String** | The latest backup status of this container. | [optional] 
**lastRefreshedAt** | **Date** | The time stamp when this container was refreshed. | [optional] 
**policyName** | **String** | The backup policy associated with this container. | [optional] 



## Enum: BackupItemTypeEnum


* `Invalid` (value: `"Invalid"`)

* `VM` (value: `"VM"`)

* `FileFolder` (value: `"FileFolder"`)

* `AzureSqlDb` (value: `"AzureSqlDb"`)

* `SQLDB` (value: `"SQLDB"`)

* `Exchange` (value: `"Exchange"`)

* `Sharepoint` (value: `"Sharepoint"`)

* `DPMUnknown` (value: `"DPMUnknown"`)




