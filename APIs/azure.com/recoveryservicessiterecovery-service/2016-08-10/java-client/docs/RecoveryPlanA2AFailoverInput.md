

# RecoveryPlanA2AFailoverInput

Recovery plan A2A failover input.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cloudServiceCreationOption** | **String** | A value indicating whether to use recovery cloud service for TFO or not. |  [optional] |
|**recoveryPointType** | [**RecoveryPointTypeEnum**](#RecoveryPointTypeEnum) | The recovery point type. |  |



## Enum: RecoveryPointTypeEnum

| Name | Value |
|---- | -----|
| LATEST | &quot;Latest&quot; |
| LATEST_APPLICATION_CONSISTENT | &quot;LatestApplicationConsistent&quot; |
| LATEST_CRASH_CONSISTENT | &quot;LatestCrashConsistent&quot; |
| LATEST_PROCESSED | &quot;LatestProcessed&quot; |



