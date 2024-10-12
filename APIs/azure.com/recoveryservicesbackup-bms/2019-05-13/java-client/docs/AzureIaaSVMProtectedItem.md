

# AzureIaaSVMProtectedItem

IaaS VM workload-specific backup item.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**extendedInfo** | [**AzureIaaSVMProtectedItemExtendedInfo**](AzureIaaSVMProtectedItemExtendedInfo.md) |  |  [optional] |
|**extendedProperties** | [**ExtendedProperties**](ExtendedProperties.md) |  |  [optional] |
|**friendlyName** | **String** | Friendly name of the VM represented by this backup item. |  [optional] |
|**healthDetails** | [**List&lt;AzureIaaSVMHealthDetails&gt;**](AzureIaaSVMHealthDetails.md) | Health details on this backup item. |  [optional] |
|**healthStatus** | [**HealthStatusEnum**](#HealthStatusEnum) | Health status of protected item |  [optional] |
|**lastBackupStatus** | **String** | Last backup operation status. |  [optional] |
|**lastBackupTime** | **OffsetDateTime** | Timestamp of the last backup operation on this backup item. |  [optional] |
|**protectedItemDataId** | **String** | Data ID of the protected item. |  [optional] |
|**protectionState** | [**ProtectionStateEnum**](#ProtectionStateEnum) | Backup state of this backup item. |  [optional] |
|**protectionStatus** | **String** | Backup status of this backup item. |  [optional] |
|**virtualMachineId** | **String** | Fully qualified ARM ID of the virtual machine represented by this item. |  [optional] |



## Enum: HealthStatusEnum

| Name | Value |
|---- | -----|
| PASSED | &quot;Passed&quot; |
| ACTION_REQUIRED | &quot;ActionRequired&quot; |
| ACTION_SUGGESTED | &quot;ActionSuggested&quot; |
| INVALID | &quot;Invalid&quot; |



## Enum: ProtectionStateEnum

| Name | Value |
|---- | -----|
| INVALID | &quot;Invalid&quot; |
| IR_PENDING | &quot;IRPending&quot; |
| PROTECTED | &quot;Protected&quot; |
| PROTECTION_ERROR | &quot;ProtectionError&quot; |
| PROTECTION_STOPPED | &quot;ProtectionStopped&quot; |
| PROTECTION_PAUSED | &quot;ProtectionPaused&quot; |



