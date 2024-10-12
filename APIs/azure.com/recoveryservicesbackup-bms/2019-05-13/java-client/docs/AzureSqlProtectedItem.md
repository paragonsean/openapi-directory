

# AzureSqlProtectedItem

Azure SQL workload-specific backup item.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**extendedInfo** | [**AzureSqlProtectedItemExtendedInfo**](AzureSqlProtectedItemExtendedInfo.md) |  |  [optional] |
|**protectedItemDataId** | **String** | Internal ID of a backup item. Used by Azure SQL Backup engine to contact Recovery Services. |  [optional] |
|**protectionState** | [**ProtectionStateEnum**](#ProtectionStateEnum) | Backup state of the backed up item. |  [optional] |



## Enum: ProtectionStateEnum

| Name | Value |
|---- | -----|
| INVALID | &quot;Invalid&quot; |
| IR_PENDING | &quot;IRPending&quot; |
| PROTECTED | &quot;Protected&quot; |
| PROTECTION_ERROR | &quot;ProtectionError&quot; |
| PROTECTION_STOPPED | &quot;ProtectionStopped&quot; |
| PROTECTION_PAUSED | &quot;ProtectionPaused&quot; |



