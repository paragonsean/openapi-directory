# SiteRecoveryManagementClient.RecoveryPlanInMageAzureV2FailoverInput

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recoveryPointType** | **String** | The recovery point type. | 
**useMultiVmSyncPoint** | **String** | A value indicating whether multi VM sync enabled VMs should use multi VM sync points for failover. | [optional] 
**vaultLocation** | **String** | The vault location. | 



## Enum: RecoveryPointTypeEnum


* `Latest` (value: `"Latest"`)

* `LatestApplicationConsistent` (value: `"LatestApplicationConsistent"`)

* `LatestCrashConsistent` (value: `"LatestCrashConsistent"`)

* `LatestProcessed` (value: `"LatestProcessed"`)




