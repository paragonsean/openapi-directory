# AndroidDeviceProvisioningPartnerApi.UnclaimDeviceRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deviceId** | **String** | Required. The device ID returned by &#x60;ClaimDevice&#x60;. | [optional] 
**deviceIdentifier** | [**DeviceIdentifier**](DeviceIdentifier.md) |  | [optional] 
**sectionType** | **String** | Required. The section type of the device&#39;s provisioning record. | [optional] 
**vacationModeDays** | **Number** | The duration of the vacation unlock starting from when the request is processed. (1 day is treated as 24 hours) | [optional] 
**vacationModeExpireTime** | **String** | The expiration time of the vacation unlock. | [optional] 



## Enum: SectionTypeEnum


* `UNSPECIFIED` (value: `"SECTION_TYPE_UNSPECIFIED"`)

* `SIM_LOCK` (value: `"SECTION_TYPE_SIM_LOCK"`)

* `ZERO_TOUCH` (value: `"SECTION_TYPE_ZERO_TOUCH"`)




