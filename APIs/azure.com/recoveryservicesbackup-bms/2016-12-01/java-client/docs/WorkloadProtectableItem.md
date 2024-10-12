

# WorkloadProtectableItem

Base class for backup item. Workload-specific backup items are derived from this class.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**backupManagementType** | **String** | Type of backup management to backup an item. |  [optional] |
|**friendlyName** | **String** | Friendly name of the backup item. |  [optional] |
|**protectableItemType** | **String** | Type of the backup item. |  [optional] |
|**protectionState** | [**ProtectionStateEnum**](#ProtectionStateEnum) | State of the back up item. |  [optional] |
|**workloadType** | **String** | Type of workload for the backup management |  [optional] |



## Enum: ProtectionStateEnum

| Name | Value |
|---- | -----|
| INVALID | &quot;Invalid&quot; |
| NOT_PROTECTED | &quot;NotProtected&quot; |
| PROTECTING | &quot;Protecting&quot; |
| PROTECTED | &quot;Protected&quot; |
| PROTECTION_FAILED | &quot;ProtectionFailed&quot; |



