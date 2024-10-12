# RecoveryServicesBackupClient.AzureIaaSVMProtectedItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extendedInfo** | [**AzureIaaSVMProtectedItemExtendedInfo**](AzureIaaSVMProtectedItemExtendedInfo.md) |  | [optional] 
**friendlyName** | **String** | The friendly name of the VM represented by this backup item. | [optional] 
**lastBackupStatus** | **String** | The last backup operation status. The possible values are: Healthy or Unhealthy. | [optional] 
**lastBackupTime** | **Date** | The timestamp of the last backup operation for this backup item. | [optional] 
**protectionState** | **String** | The backup state of this backup item. | [optional] 
**protectionStatus** | **String** | The backup status of this backup item. | [optional] 
**virtualMachineId** | **String** | The fully qualified Resource Manager ID of the virtual machine represented by this item. | [optional] 



## Enum: ProtectionStateEnum


* `Invalid` (value: `"Invalid"`)

* `IRPending` (value: `"IRPending"`)

* `Protected` (value: `"Protected"`)

* `ProtectionError` (value: `"ProtectionError"`)

* `ProtectionStopped` (value: `"ProtectionStopped"`)

* `ProtectionPaused` (value: `"ProtectionPaused"`)




