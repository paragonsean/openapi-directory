

# AzureIaaSVMProtectedItem

This Azure VM workload-specific (also known as IaaS VM workload-specific) backup item has been backed up.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**extendedInfo** | [**AzureIaaSVMProtectedItemExtendedInfo**](AzureIaaSVMProtectedItemExtendedInfo.md) |  |  [optional] |
|**friendlyName** | **String** | The friendly name of the VM represented by this backup item. |  [optional] |
|**lastBackupStatus** | **String** | The last backup operation status. The possible values are: Healthy or Unhealthy. |  [optional] |
|**lastBackupTime** | **OffsetDateTime** | The timestamp of the last backup operation for this backup item. |  [optional] |
|**protectionState** | [**ProtectionStateEnum**](#ProtectionStateEnum) | The backup state of this backup item. |  [optional] |
|**protectionStatus** | **String** | The backup status of this backup item. |  [optional] |
|**virtualMachineId** | **String** | The fully qualified Resource Manager ID of the virtual machine represented by this item. |  [optional] |



## Enum: ProtectionStateEnum

| Name | Value |
|---- | -----|
| INVALID | &quot;Invalid&quot; |
| IR_PENDING | &quot;IRPending&quot; |
| PROTECTED | &quot;Protected&quot; |
| PROTECTION_ERROR | &quot;ProtectionError&quot; |
| PROTECTION_STOPPED | &quot;ProtectionStopped&quot; |
| PROTECTION_PAUSED | &quot;ProtectionPaused&quot; |



