# SiteRecoveryManagementClient.RecoveryPlanA2AFailoverInput

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloudServiceCreationOption** | **String** | A value indicating whether to use recovery cloud service for TFO or not. | [optional] 
**multiVmSyncPointOption** | **String** | A value indicating whether multi VM sync enabled VMs should use multi VM sync points for failover. | [optional] 
**recoveryPointType** | **String** | The recovery point type. | 



## Enum: MultiVmSyncPointOptionEnum


* `UseMultiVmSyncRecoveryPoint` (value: `"UseMultiVmSyncRecoveryPoint"`)

* `UsePerVmRecoveryPoint` (value: `"UsePerVmRecoveryPoint"`)





## Enum: RecoveryPointTypeEnum


* `Latest` (value: `"Latest"`)

* `LatestApplicationConsistent` (value: `"LatestApplicationConsistent"`)

* `LatestCrashConsistent` (value: `"LatestCrashConsistent"`)

* `LatestProcessed` (value: `"LatestProcessed"`)




