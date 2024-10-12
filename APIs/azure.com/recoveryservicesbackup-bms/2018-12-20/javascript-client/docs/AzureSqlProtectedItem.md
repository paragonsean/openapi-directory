# RecoveryServicesBackupClient.AzureSqlProtectedItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extendedInfo** | [**AzureSqlProtectedItemExtendedInfo**](AzureSqlProtectedItemExtendedInfo.md) |  | [optional] 
**protectedItemDataId** | **String** | Internal ID of a backup item. Used by Azure SQL Backup engine to contact Recovery Services. | [optional] 
**protectionState** | **String** | Backup state of the backed up item. | [optional] 



## Enum: ProtectionStateEnum


* `Invalid` (value: `"Invalid"`)

* `IRPending` (value: `"IRPending"`)

* `Protected` (value: `"Protected"`)

* `ProtectionError` (value: `"ProtectionError"`)

* `ProtectionStopped` (value: `"ProtectionStopped"`)

* `ProtectionPaused` (value: `"ProtectionPaused"`)




