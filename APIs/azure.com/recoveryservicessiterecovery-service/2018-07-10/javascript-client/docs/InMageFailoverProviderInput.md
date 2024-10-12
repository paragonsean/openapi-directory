# SiteRecoveryManagementClient.InMageFailoverProviderInput

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recoveryPointId** | **String** | The recovery point id to be passed to failover to a particular recovery point. In case of latest recovery point, null should be passed. | [optional] 
**recoveryPointType** | **String** | The recovery point type. Values from LatestTime, LatestTag or Custom. In the case of custom, the recovery point provided by RecoveryPointId will be used. In the other two cases, recovery point id will be ignored. | [optional] 



## Enum: RecoveryPointTypeEnum


* `LatestTime` (value: `"LatestTime"`)

* `LatestTag` (value: `"LatestTag"`)

* `Custom` (value: `"Custom"`)




