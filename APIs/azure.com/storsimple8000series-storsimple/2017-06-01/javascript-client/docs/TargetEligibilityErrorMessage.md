# StorSimple8000SeriesManagementClient.TargetEligibilityErrorMessage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **String** | The localized error message stating the reason why the device is not eligible as a target device. | [optional] 
**resolution** | **String** | The localized resolution message for the error. | [optional] 
**resultCode** | **String** | The result code for the error, due to which the device does not qualify as a failover target device. | [optional] 



## Enum: ResultCodeEnum


* `TargetAndSourceCannotBeSameError` (value: `"TargetAndSourceCannotBeSameError"`)

* `TargetIsNotOnlineError` (value: `"TargetIsNotOnlineError"`)

* `TargetSourceIncompatibleVersionError` (value: `"TargetSourceIncompatibleVersionError"`)

* `LocalToTieredVolumesConversionWarning` (value: `"LocalToTieredVolumesConversionWarning"`)

* `TargetInsufficientCapacityError` (value: `"TargetInsufficientCapacityError"`)

* `TargetInsufficientLocalVolumeMemoryError` (value: `"TargetInsufficientLocalVolumeMemoryError"`)

* `TargetInsufficientTieredVolumeMemoryError` (value: `"TargetInsufficientTieredVolumeMemoryError"`)




