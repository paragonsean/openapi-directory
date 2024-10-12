

# DeviceClaim

A record of a device claimed by a reseller for a customer. Devices claimed for zero-touch enrollment have a claim with the type `SECTION_TYPE_ZERO_TOUCH`. To learn more, read [Claim devices for customers](/zero-touch/guides/how-it-works#claim).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**additionalService** | [**AdditionalServiceEnum**](#AdditionalServiceEnum) | The Additional service registered for the device. |  [optional] |
|**googleWorkspaceCustomerId** | **String** | The ID of the Google Workspace account that owns the Chrome OS device. |  [optional] |
|**ownerCompanyId** | **String** | The ID of the Customer that purchased the device. |  [optional] |
|**resellerId** | **String** | The ID of the reseller that claimed the device. |  [optional] |
|**sectionType** | [**SectionTypeEnum**](#SectionTypeEnum) | Output only. The type of claim made on the device. |  [optional] [readonly] |
|**vacationModeExpireTime** | **String** | The timestamp when the device will exit ‘vacation mode’. This value is present iff the device is in &#39;vacation mode&#39;. |  [optional] |
|**vacationModeStartTime** | **String** | The timestamp when the device was put into ‘vacation mode’. This value is present iff the device is in &#39;vacation mode&#39;. |  [optional] |



## Enum: AdditionalServiceEnum

| Name | Value |
|---- | -----|
| ADDITIONAL_SERVICE_UNSPECIFIED | &quot;ADDITIONAL_SERVICE_UNSPECIFIED&quot; |
| DEVICE_PROTECTION | &quot;DEVICE_PROTECTION&quot; |



## Enum: SectionTypeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;SECTION_TYPE_UNSPECIFIED&quot; |
| SIM_LOCK | &quot;SECTION_TYPE_SIM_LOCK&quot; |
| ZERO_TOUCH | &quot;SECTION_TYPE_ZERO_TOUCH&quot; |



