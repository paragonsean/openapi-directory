

# TargetEligibilityErrorMessage

The error/warning message due to which the device is ineligible as a failover target device.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**message** | **String** | The localized error message stating the reason why the device is not eligible as a target device. |  [optional] |
|**resolution** | **String** | The localized resolution message for the error. |  [optional] |
|**resultCode** | [**ResultCodeEnum**](#ResultCodeEnum) | The result code for the error, due to which the device does not qualify as a failover target device. |  [optional] |



## Enum: ResultCodeEnum

| Name | Value |
|---- | -----|
| TARGET_AND_SOURCE_CANNOT_BE_SAME_ERROR | &quot;TargetAndSourceCannotBeSameError&quot; |
| TARGET_IS_NOT_ONLINE_ERROR | &quot;TargetIsNotOnlineError&quot; |
| TARGET_SOURCE_INCOMPATIBLE_VERSION_ERROR | &quot;TargetSourceIncompatibleVersionError&quot; |
| LOCAL_TO_TIERED_VOLUMES_CONVERSION_WARNING | &quot;LocalToTieredVolumesConversionWarning&quot; |
| TARGET_INSUFFICIENT_CAPACITY_ERROR | &quot;TargetInsufficientCapacityError&quot; |
| TARGET_INSUFFICIENT_LOCAL_VOLUME_MEMORY_ERROR | &quot;TargetInsufficientLocalVolumeMemoryError&quot; |
| TARGET_INSUFFICIENT_TIERED_VOLUME_MEMORY_ERROR | &quot;TargetInsufficientTieredVolumeMemoryError&quot; |



