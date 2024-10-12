# RecoveryServicesBackupClient.AzureFileshareProtectedItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extendedInfo** | [**AzureFileshareProtectedItemExtendedInfo**](AzureFileshareProtectedItemExtendedInfo.md) |  | [optional] 
**friendlyName** | **String** | Friendly name of the fileshare represented by this backup item. | [optional] 
**healthStatus** | **String** | backups running status for this backup item. | [optional] 
**lastBackupStatus** | **String** | Last backup operation status. Possible values: Healthy, Unhealthy. | [optional] 
**lastBackupTime** | **Date** | Timestamp of the last backup operation on this backup item. | [optional] 
**protectionState** | **String** | Backup state of this backup item. | [optional] 
**protectionStatus** | **String** | Backup status of this backup item. | [optional] 



## Enum: HealthStatusEnum


* `Passed` (value: `"Passed"`)

* `ActionRequired` (value: `"ActionRequired"`)

* `ActionSuggested` (value: `"ActionSuggested"`)

* `Invalid` (value: `"Invalid"`)





## Enum: ProtectionStateEnum


* `Invalid` (value: `"Invalid"`)

* `IRPending` (value: `"IRPending"`)

* `Protected` (value: `"Protected"`)

* `ProtectionError` (value: `"ProtectionError"`)

* `ProtectionStopped` (value: `"ProtectionStopped"`)

* `ProtectionPaused` (value: `"ProtectionPaused"`)




