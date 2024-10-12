# RecoveryServicesBackupClient.AzureIaaSVMProtectedItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extendedInfo** | [**AzureIaaSVMProtectedItemExtendedInfo**](AzureIaaSVMProtectedItemExtendedInfo.md) |  | [optional] 
**extendedProperties** | [**ExtendedProperties**](ExtendedProperties.md) |  | [optional] 
**friendlyName** | **String** | Friendly name of the VM represented by this backup item. | [optional] 
**healthDetails** | [**[AzureIaaSVMHealthDetails]**](AzureIaaSVMHealthDetails.md) | Health details on this backup item. | [optional] 
**healthStatus** | **String** | Health status of protected item | [optional] 
**lastBackupStatus** | **String** | Last backup operation status. | [optional] 
**lastBackupTime** | **Date** | Timestamp of the last backup operation on this backup item. | [optional] 
**protectedItemDataId** | **String** | Data ID of the protected item. | [optional] 
**protectionState** | **String** | Backup state of this backup item. | [optional] 
**protectionStatus** | **String** | Backup status of this backup item. | [optional] 
**virtualMachineId** | **String** | Fully qualified ARM ID of the virtual machine represented by this item. | [optional] 



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




