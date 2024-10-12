

# DPMProtectedItem

Additional information on Backup engine specific backup item.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**backupEngineName** | **String** | Backup Management server protecting this backup item |  [optional] |
|**extendedInfo** | [**DPMProtectedItemExtendedInfo**](DPMProtectedItemExtendedInfo.md) |  |  [optional] |
|**friendlyName** | **String** | Friendly name of the managed item |  [optional] |
|**protectionState** | [**ProtectionStateEnum**](#ProtectionStateEnum) | Protection state of the backup engine |  [optional] |



## Enum: ProtectionStateEnum

| Name | Value |
|---- | -----|
| INVALID | &quot;Invalid&quot; |
| IR_PENDING | &quot;IRPending&quot; |
| PROTECTED | &quot;Protected&quot; |
| PROTECTION_ERROR | &quot;ProtectionError&quot; |
| PROTECTION_STOPPED | &quot;ProtectionStopped&quot; |
| PROTECTION_PAUSED | &quot;ProtectionPaused&quot; |



