

# CacheUpgradeStatus

Properties describing the software upgrade state of the cache

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**currentFirmwareVersion** | **String** | Version string of the firmware currently installed on this cache. |  [optional] [readonly] |
|**firmwareUpdateDeadline** | **OffsetDateTime** | Time at which the pending firmware update will automatically be installed on the cache. |  [optional] [readonly] |
|**firmwareUpdateStatus** | [**FirmwareUpdateStatusEnum**](#FirmwareUpdateStatusEnum) | True if there is a firmware update ready to install on this cache.  The firmware will automatically be installed after firmwareUpdateDeadline if not triggered earlier via the upgrade operation. |  [optional] [readonly] |
|**lastFirmwareUpdate** | **OffsetDateTime** | Time of the last successful firmware update. |  [optional] [readonly] |
|**pendingFirmwareVersion** | **String** | When firmwareUpdateAvailable is true, this field holds the version string for the update. |  [optional] [readonly] |



## Enum: FirmwareUpdateStatusEnum

| Name | Value |
|---- | -----|
| AVAILABLE | &quot;available&quot; |
| UNAVAILABLE | &quot;unavailable&quot; |



