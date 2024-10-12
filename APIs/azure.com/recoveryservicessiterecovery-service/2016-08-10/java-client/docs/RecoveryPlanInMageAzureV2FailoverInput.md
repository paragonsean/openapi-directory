

# RecoveryPlanInMageAzureV2FailoverInput

Recovery plan InMageAzureV2 failover input.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**recoveryPointType** | [**RecoveryPointTypeEnum**](#RecoveryPointTypeEnum) | The recovery point type. |  |
|**useMultiVmSyncPoint** | **String** | A value indicating whether multi VM sync enabled VMs should use multi VM sync points for failover. |  [optional] |
|**vaultLocation** | **String** | The vault location. |  |



## Enum: RecoveryPointTypeEnum

| Name | Value |
|---- | -----|
| LATEST | &quot;Latest&quot; |
| LATEST_APPLICATION_CONSISTENT | &quot;LatestApplicationConsistent&quot; |
| LATEST_CRASH_CONSISTENT | &quot;LatestCrashConsistent&quot; |
| LATEST_PROCESSED | &quot;LatestProcessed&quot; |



