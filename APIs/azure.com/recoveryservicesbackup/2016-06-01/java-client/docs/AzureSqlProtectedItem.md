

# AzureSqlProtectedItem

This is an Azure SQL workload-specific backup item.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**extendedInfo** | [**AzureSqlProtectedItemExtendedInfo**](AzureSqlProtectedItemExtendedInfo.md) |  |  [optional] |
|**protectedItemDataId** | **String** | The internal ID of a backup item. The internal ID is used by the Azure SQL Backup engine to contact Recovery Services. |  [optional] |
|**protectionState** | [**ProtectionStateEnum**](#ProtectionStateEnum) | The backup state of the backup item. |  [optional] |



## Enum: ProtectionStateEnum

| Name | Value |
|---- | -----|
| INVALID | &quot;Invalid&quot; |
| IR_PENDING | &quot;IRPending&quot; |
| PROTECTED | &quot;Protected&quot; |
| PROTECTION_ERROR | &quot;ProtectionError&quot; |
| PROTECTION_STOPPED | &quot;ProtectionStopped&quot; |
| PROTECTION_PAUSED | &quot;ProtectionPaused&quot; |



