

# A2ARecoveryPointDetails

A2A provider specific recovery point details.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**disks** | **List&lt;String&gt;** | List of disk ids representing a recovery point. |  [optional] |
|**recoveryPointSyncType** | [**RecoveryPointSyncTypeEnum**](#RecoveryPointSyncTypeEnum) | A value indicating whether the recovery point is multi VM consistent. |  [optional] |



## Enum: RecoveryPointSyncTypeEnum

| Name | Value |
|---- | -----|
| MULTI_VM_SYNC_RECOVERY_POINT | &quot;MultiVmSyncRecoveryPoint&quot; |
| PER_VM_RECOVERY_POINT | &quot;PerVmRecoveryPoint&quot; |



