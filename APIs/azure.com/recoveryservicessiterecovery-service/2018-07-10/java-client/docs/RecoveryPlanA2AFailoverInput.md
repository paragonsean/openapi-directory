

# RecoveryPlanA2AFailoverInput

Recovery plan A2A failover input.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cloudServiceCreationOption** | **String** | A value indicating whether to use recovery cloud service for TFO or not. |  [optional] |
|**multiVmSyncPointOption** | [**MultiVmSyncPointOptionEnum**](#MultiVmSyncPointOptionEnum) | A value indicating whether multi VM sync enabled VMs should use multi VM sync points for failover. |  [optional] |
|**recoveryPointType** | [**RecoveryPointTypeEnum**](#RecoveryPointTypeEnum) | The recovery point type. |  |



## Enum: MultiVmSyncPointOptionEnum

| Name | Value |
|---- | -----|
| USE_MULTI_VM_SYNC_RECOVERY_POINT | &quot;UseMultiVmSyncRecoveryPoint&quot; |
| USE_PER_VM_RECOVERY_POINT | &quot;UsePerVmRecoveryPoint&quot; |



## Enum: RecoveryPointTypeEnum

| Name | Value |
|---- | -----|
| LATEST | &quot;Latest&quot; |
| LATEST_APPLICATION_CONSISTENT | &quot;LatestApplicationConsistent&quot; |
| LATEST_CRASH_CONSISTENT | &quot;LatestCrashConsistent&quot; |
| LATEST_PROCESSED | &quot;LatestProcessed&quot; |



