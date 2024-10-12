

# UnclaimDeviceRequest

Request message to unclaim a device.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**deviceId** | **String** | Required. The device ID returned by &#x60;ClaimDevice&#x60;. |  [optional] |
|**deviceIdentifier** | [**DeviceIdentifier**](DeviceIdentifier.md) |  |  [optional] |
|**sectionType** | [**SectionTypeEnum**](#SectionTypeEnum) | Required. The section type of the device&#39;s provisioning record. |  [optional] |
|**vacationModeDays** | **Integer** | The duration of the vacation unlock starting from when the request is processed. (1 day is treated as 24 hours) |  [optional] |
|**vacationModeExpireTime** | **String** | The expiration time of the vacation unlock. |  [optional] |



## Enum: SectionTypeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;SECTION_TYPE_UNSPECIFIED&quot; |
| SIM_LOCK | &quot;SECTION_TYPE_SIM_LOCK&quot; |
| ZERO_TOUCH | &quot;SECTION_TYPE_ZERO_TOUCH&quot; |



