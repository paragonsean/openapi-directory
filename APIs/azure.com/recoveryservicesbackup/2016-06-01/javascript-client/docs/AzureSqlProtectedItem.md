# RecoveryServicesBackupClient.AzureSqlProtectedItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extendedInfo** | [**AzureSqlProtectedItemExtendedInfo**](AzureSqlProtectedItemExtendedInfo.md) |  | [optional] 
**protectedItemDataId** | **String** | The internal ID of a backup item. The internal ID is used by the Azure SQL Backup engine to contact Recovery Services. | [optional] 
**protectionState** | **String** | The backup state of the backup item. | [optional] 



## Enum: ProtectionStateEnum


* `Invalid` (value: `"Invalid"`)

* `IRPending` (value: `"IRPending"`)

* `Protected` (value: `"Protected"`)

* `ProtectionError` (value: `"ProtectionError"`)

* `ProtectionStopped` (value: `"ProtectionStopped"`)

* `ProtectionPaused` (value: `"ProtectionPaused"`)




