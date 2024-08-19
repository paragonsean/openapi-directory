

# PerAndroidVersionInfo

A version-specific information of an Android model.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**deviceCapacity** | [**DeviceCapacityEnum**](#DeviceCapacityEnum) | The number of online devices for an Android version. |  [optional] |
|**directAccessVersionInfo** | [**DirectAccessVersionInfo**](DirectAccessVersionInfo.md) |  |  [optional] |
|**interactiveDeviceAvailabilityEstimate** | **String** | Output only. The estimated wait time for a single interactive device session using Direct Access. |  [optional] [readonly] |
|**versionId** | **String** | An Android version. |  [optional] |



## Enum: DeviceCapacityEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;DEVICE_CAPACITY_UNSPECIFIED&quot; |
| HIGH | &quot;DEVICE_CAPACITY_HIGH&quot; |
| MEDIUM | &quot;DEVICE_CAPACITY_MEDIUM&quot; |
| LOW | &quot;DEVICE_CAPACITY_LOW&quot; |
| NONE | &quot;DEVICE_CAPACITY_NONE&quot; |



