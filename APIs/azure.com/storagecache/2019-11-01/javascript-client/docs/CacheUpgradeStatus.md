# StorageCacheMgmtClient.CacheUpgradeStatus

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currentFirmwareVersion** | **String** | Version string of the firmware currently installed on this Cache. | [optional] [readonly] 
**firmwareUpdateDeadline** | **Date** | Time at which the pending firmware update will automatically be installed on the Cache. | [optional] [readonly] 
**firmwareUpdateStatus** | **String** | True if there is a firmware update ready to install on this Cache. The firmware will automatically be installed after firmwareUpdateDeadline if not triggered earlier via the upgrade operation. | [optional] [readonly] 
**lastFirmwareUpdate** | **Date** | Time of the last successful firmware update. | [optional] [readonly] 
**pendingFirmwareVersion** | **String** | When firmwareUpdateAvailable is true, this field holds the version string for the update. | [optional] [readonly] 



## Enum: FirmwareUpdateStatusEnum


* `available` (value: `"available"`)

* `unavailable` (value: `"unavailable"`)




