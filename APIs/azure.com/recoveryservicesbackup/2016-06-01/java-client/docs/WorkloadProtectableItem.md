

# WorkloadProtectableItem

The base class for backup item. Workload-specific backup items are derived from this class.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**backupManagementType** | **String** | The backup management type. |  [optional] |
|**friendlyName** | **String** | The friendly name of the backup item. |  [optional] |
|**protectableItemType** | **String** | The type of the backup item. |  [optional] |
|**protectionState** | [**ProtectionStateEnum**](#ProtectionStateEnum) | The state of the back up item. |  [optional] |



## Enum: ProtectionStateEnum

| Name | Value |
|---- | -----|
| INVALID | &quot;Invalid&quot; |
| NOT_PROTECTED | &quot;NotProtected&quot; |
| PROTECTING | &quot;Protecting&quot; |
| PROTECTED | &quot;Protected&quot; |



