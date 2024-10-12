

# RcmAzureMigrationPolicyDetails

RCM based Azure migration specific policy details.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**appConsistentFrequencyInMinutes** | **Integer** | The app consistent snapshot frequency in minutes. |  [optional] |
|**crashConsistentFrequencyInMinutes** | **Integer** | The crash consistent snapshot frequency in minutes. |  [optional] |
|**multiVmSyncStatus** | [**MultiVmSyncStatusEnum**](#MultiVmSyncStatusEnum) | A value indicating whether multi-VM sync has to be enabled. |  [optional] |
|**recoveryPointHistory** | **Integer** | The duration in minutes until which the recovery points need to be stored. |  [optional] |
|**recoveryPointThresholdInMinutes** | **Integer** | The recovery point threshold in minutes. |  [optional] |



## Enum: MultiVmSyncStatusEnum

| Name | Value |
|---- | -----|
| ENABLED | &quot;Enabled&quot; |
| DISABLED | &quot;Disabled&quot; |



