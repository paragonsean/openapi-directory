

# PartnerUnclaim

Identifies one unclaim request.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**deviceId** | **String** | Required. Device ID of the device. |  [optional] |
|**deviceIdentifier** | [**DeviceIdentifier**](DeviceIdentifier.md) |  |  [optional] |
|**sectionType** | [**SectionTypeEnum**](#SectionTypeEnum) | Required. The section type of the device&#39;s provisioning record. |  [optional] |
|**vacationModeDays** | **Integer** | Optional. The duration of the vacation unlock starting from when the request is processed. (1 day is treated as 24 hours) |  [optional] |
|**vacationModeExpireTime** | **String** | Optional. The expiration time of the vacation unlock. |  [optional] |



## Enum: SectionTypeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;SECTION_TYPE_UNSPECIFIED&quot; |
| SIM_LOCK | &quot;SECTION_TYPE_SIM_LOCK&quot; |
| ZERO_TOUCH | &quot;SECTION_TYPE_ZERO_TOUCH&quot; |



