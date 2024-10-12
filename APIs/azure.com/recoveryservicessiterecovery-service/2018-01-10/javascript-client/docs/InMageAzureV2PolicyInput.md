# SiteRecoveryManagementClient.InMageAzureV2PolicyInput

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appConsistentFrequencyInMinutes** | **Number** | The app consistent snapshot frequency (in minutes). | [optional] 
**crashConsistentFrequencyInMinutes** | **Number** | The crash consistent snapshot frequency (in minutes). | [optional] 
**multiVmSyncStatus** | **String** | A value indicating whether multi-VM sync has to be enabled. Value should be &#39;Enabled&#39; or &#39;Disabled&#39;. | 
**recoveryPointHistory** | **Number** | The duration in minutes until which the recovery points need to be stored. | [optional] 
**recoveryPointThresholdInMinutes** | **Number** | The recovery point threshold in minutes. | [optional] 



## Enum: MultiVmSyncStatusEnum


* `Enable` (value: `"Enable"`)

* `Disable` (value: `"Disable"`)




