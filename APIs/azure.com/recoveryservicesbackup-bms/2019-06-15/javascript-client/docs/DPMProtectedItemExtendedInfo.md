# RecoveryServicesBackupClient.DPMProtectedItemExtendedInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**diskStorageUsedInBytes** | **String** | Used Disk storage in bytes. | [optional] 
**isCollocated** | **Boolean** | To check if backup item is collocated. | [optional] 
**isPresentOnCloud** | **Boolean** | To check if backup item is cloud protected. | [optional] 
**lastBackupStatus** | **String** | Last backup status information on backup item. | [optional] 
**lastRefreshedAt** | **Date** | Last refresh time on backup item. | [optional] 
**oldestRecoveryPoint** | **Date** | Oldest cloud recovery point time. | [optional] 
**onPremiseLatestRecoveryPoint** | **Date** | latest disk recovery point time. | [optional] 
**onPremiseOldestRecoveryPoint** | **Date** | Oldest disk recovery point time. | [optional] 
**onPremiseRecoveryPointCount** | **Number** | disk recovery point count. | [optional] 
**protectableObjectLoadPath** | **{String: String}** | Attribute to provide information on various DBs. | [optional] 
**_protected** | **Boolean** | To check if backup item is disk protected. | [optional] 
**protectionGroupName** | **String** | Protection group name of the backup item. | [optional] 
**recoveryPointCount** | **Number** | cloud recovery point count. | [optional] 
**totalDiskStorageSizeInBytes** | **String** | total Disk storage in bytes. | [optional] 


