# AndroidDeviceProvisioningPartnerApi.DeviceClaim

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additionalService** | **String** | The Additional service registered for the device. | [optional] 
**googleWorkspaceCustomerId** | **String** | The ID of the Google Workspace account that owns the Chrome OS device. | [optional] 
**ownerCompanyId** | **String** | The ID of the Customer that purchased the device. | [optional] 
**resellerId** | **String** | The ID of the reseller that claimed the device. | [optional] 
**sectionType** | **String** | Output only. The type of claim made on the device. | [optional] [readonly] 
**vacationModeExpireTime** | **String** | The timestamp when the device will exit ‘vacation mode’. This value is present iff the device is in &#39;vacation mode&#39;. | [optional] 
**vacationModeStartTime** | **String** | The timestamp when the device was put into ‘vacation mode’. This value is present iff the device is in &#39;vacation mode&#39;. | [optional] 



## Enum: AdditionalServiceEnum


* `ADDITIONAL_SERVICE_UNSPECIFIED` (value: `"ADDITIONAL_SERVICE_UNSPECIFIED"`)

* `DEVICE_PROTECTION` (value: `"DEVICE_PROTECTION"`)





## Enum: SectionTypeEnum


* `UNSPECIFIED` (value: `"SECTION_TYPE_UNSPECIFIED"`)

* `SIM_LOCK` (value: `"SECTION_TYPE_SIM_LOCK"`)

* `ZERO_TOUCH` (value: `"SECTION_TYPE_ZERO_TOUCH"`)




