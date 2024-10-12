

# AzureFileshareProtectedItem

Azure File Share workload-specific backup item.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**extendedInfo** | [**AzureFileshareProtectedItemExtendedInfo**](AzureFileshareProtectedItemExtendedInfo.md) |  |  [optional] |
|**friendlyName** | **String** | Friendly name of the fileshare represented by this backup item. |  [optional] |
|**healthStatus** | [**HealthStatusEnum**](#HealthStatusEnum) | backups running status for this backup item. |  [optional] |
|**lastBackupStatus** | **String** | Last backup operation status. Possible values: Healthy, Unhealthy. |  [optional] |
|**lastBackupTime** | **OffsetDateTime** | Timestamp of the last backup operation on this backup item. |  [optional] |
|**protectionState** | [**ProtectionStateEnum**](#ProtectionStateEnum) | Backup state of this backup item. |  [optional] |
|**protectionStatus** | **String** | Backup status of this backup item. |  [optional] |



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



