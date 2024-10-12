

# InMageAzureV2PolicyInput

VMWare Azure specific policy Input.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**appConsistentFrequencyInMinutes** | **Integer** | The app consistent snapshot frequency (in minutes). |  [optional] |
|**crashConsistentFrequencyInMinutes** | **Integer** | The crash consistent snapshot frequency (in minutes). |  [optional] |
|**multiVmSyncStatus** | [**MultiVmSyncStatusEnum**](#MultiVmSyncStatusEnum) | A value indicating whether multi-VM sync has to be enabled. Value should be &#39;Enabled&#39; or &#39;Disabled&#39;. |  |
|**recoveryPointHistory** | **Integer** | The duration in minutes until which the recovery points need to be stored. |  [optional] |
|**recoveryPointThresholdInMinutes** | **Integer** | The recovery point threshold in minutes. |  [optional] |



## Enum: MultiVmSyncStatusEnum

| Name | Value |
|---- | -----|
| ENABLE | &quot;Enable&quot; |
| DISABLE | &quot;Disable&quot; |



