

# AzureWorkloadRestoreRequest

AzureWorkload-specific restore.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**propertyBag** | **Map&lt;String, String&gt;** | Workload specific property bag. |  [optional] |
|**recoveryMode** | [**RecoveryModeEnum**](#RecoveryModeEnum) | Defines whether the current recovery mode is file restore or database restore |  [optional] |
|**recoveryType** | [**RecoveryTypeEnum**](#RecoveryTypeEnum) | Type of this recovery. |  [optional] |
|**sourceResourceId** | **String** | Fully qualified ARM ID of the VM on which workload that was running is being recovered. |  [optional] |
|**targetInfo** | [**TargetRestoreInfo**](TargetRestoreInfo.md) |  |  [optional] |



## Enum: RecoveryModeEnum

| Name | Value |
|---- | -----|
| INVALID | &quot;Invalid&quot; |
| FILE_RECOVERY | &quot;FileRecovery&quot; |
| WORKLOAD_RECOVERY | &quot;WorkloadRecovery&quot; |



## Enum: RecoveryTypeEnum

| Name | Value |
|---- | -----|
| INVALID | &quot;Invalid&quot; |
| ORIGINAL_LOCATION | &quot;OriginalLocation&quot; |
| ALTERNATE_LOCATION | &quot;AlternateLocation&quot; |
| RESTORE_DISKS | &quot;RestoreDisks&quot; |
| OFFLINE | &quot;Offline&quot; |



