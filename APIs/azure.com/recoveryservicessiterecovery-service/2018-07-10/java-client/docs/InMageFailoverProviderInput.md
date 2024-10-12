

# InMageFailoverProviderInput

Provider specific input for InMage failover.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**recoveryPointId** | **String** | The recovery point id to be passed to failover to a particular recovery point. In case of latest recovery point, null should be passed. |  [optional] |
|**recoveryPointType** | [**RecoveryPointTypeEnum**](#RecoveryPointTypeEnum) | The recovery point type. Values from LatestTime, LatestTag or Custom. In the case of custom, the recovery point provided by RecoveryPointId will be used. In the other two cases, recovery point id will be ignored. |  [optional] |



## Enum: RecoveryPointTypeEnum

| Name | Value |
|---- | -----|
| LATEST_TIME | &quot;LatestTime&quot; |
| LATEST_TAG | &quot;LatestTag&quot; |
| CUSTOM | &quot;Custom&quot; |



