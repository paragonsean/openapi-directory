

# AzureVmWorkloadProtectedItem

Azure VM workload-specific protected item.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**extendedInfo** | [**AzureVmWorkloadProtectedItemExtendedInfo**](AzureVmWorkloadProtectedItemExtendedInfo.md) |  |  [optional] |
|**friendlyName** | **String** | Friendly name of the DB represented by this backup item. |  [optional] |
|**lastBackupErrorDetail** | [**ErrorDetail**](ErrorDetail.md) |  |  [optional] |
|**lastBackupStatus** | [**LastBackupStatusEnum**](#LastBackupStatusEnum) | Last backup operation status. Possible values: Healthy, Unhealthy. |  [optional] |
|**lastBackupTime** | **OffsetDateTime** | Timestamp of the last backup operation on this backup item. |  [optional] |
|**parentName** | **String** | Parent name of the DB such as Instance or Availability Group. |  [optional] |
|**parentType** | **String** | Parent type of protected item, example: for a DB, standalone server or distributed |  [optional] |
|**protectedItemDataSourceId** | **String** | Data ID of the protected item. |  [optional] |
|**protectedItemHealthStatus** | [**ProtectedItemHealthStatusEnum**](#ProtectedItemHealthStatusEnum) | Health status of the backup item, evaluated based on last heartbeat received |  [optional] |
|**protectionState** | [**ProtectionStateEnum**](#ProtectionStateEnum) | Backup state of this backup item. |  [optional] |
|**protectionStatus** | **String** | Backup status of this backup item. |  [optional] |
|**serverName** | **String** | Host/Cluster Name for instance or AG |  [optional] |



## Enum: LastBackupStatusEnum

| Name | Value |
|---- | -----|
| INVALID | &quot;Invalid&quot; |
| HEALTHY | &quot;Healthy&quot; |
| UNHEALTHY | &quot;Unhealthy&quot; |
| IR_PENDING | &quot;IRPending&quot; |



## Enum: ProtectedItemHealthStatusEnum

| Name | Value |
|---- | -----|
| INVALID | &quot;Invalid&quot; |
| HEALTHY | &quot;Healthy&quot; |
| UNHEALTHY | &quot;Unhealthy&quot; |
| NOT_REACHABLE | &quot;NotReachable&quot; |
| IR_PENDING | &quot;IRPending&quot; |



## Enum: ProtectionStateEnum

| Name | Value |
|---- | -----|
| INVALID | &quot;Invalid&quot; |
| IR_PENDING | &quot;IRPending&quot; |
| PROTECTED | &quot;Protected&quot; |
| PROTECTION_ERROR | &quot;ProtectionError&quot; |
| PROTECTION_STOPPED | &quot;ProtectionStopped&quot; |
| PROTECTION_PAUSED | &quot;ProtectionPaused&quot; |



