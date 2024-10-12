# RecoveryServicesBackupClient.AzureWorkloadRestoreRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**propertyBag** | **{String: String}** | Workload specific property bag. | [optional] 
**recoveryMode** | **String** | Defines whether the current recovery mode is file restore or database restore | [optional] 
**recoveryType** | **String** | Type of this recovery. | [optional] 
**sourceResourceId** | **String** | Fully qualified ARM ID of the VM on which workload that was running is being recovered. | [optional] 
**targetInfo** | [**TargetRestoreInfo**](TargetRestoreInfo.md) |  | [optional] 



## Enum: RecoveryModeEnum


* `Invalid` (value: `"Invalid"`)

* `FileRecovery` (value: `"FileRecovery"`)

* `WorkloadRecovery` (value: `"WorkloadRecovery"`)





## Enum: RecoveryTypeEnum


* `Invalid` (value: `"Invalid"`)

* `OriginalLocation` (value: `"OriginalLocation"`)

* `AlternateLocation` (value: `"AlternateLocation"`)

* `RestoreDisks` (value: `"RestoreDisks"`)

* `Offline` (value: `"Offline"`)




