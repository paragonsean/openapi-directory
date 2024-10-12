# AndroidDeviceProvisioningPartnerApi.ClaimDeviceRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configurationId** | **String** | Optional. The ID of the configuration applied to the device section. | [optional] 
**customerId** | **String** | The ID of the customer for whom the device is being claimed. | [optional] 
**deviceIdentifier** | [**DeviceIdentifier**](DeviceIdentifier.md) |  | [optional] 
**deviceMetadata** | [**DeviceMetadata**](DeviceMetadata.md) |  | [optional] 
**googleWorkspaceCustomerId** | **String** | The Google Workspace customer ID. | [optional] 
**preProvisioningToken** | **String** | Optional. Must and can only be set for Chrome OS devices. | [optional] 
**sectionType** | **String** | Required. The section type of the device&#39;s provisioning record. | [optional] 
**simlockProfileId** | **String** | Optional. Must and can only be set when DeviceProvisioningSectionType is SECTION_TYPE_SIM_LOCK. The unique identifier of the SimLock profile. | [optional] 



## Enum: SectionTypeEnum


* `UNSPECIFIED` (value: `"SECTION_TYPE_UNSPECIFIED"`)

* `SIM_LOCK` (value: `"SECTION_TYPE_SIM_LOCK"`)

* `ZERO_TOUCH` (value: `"SECTION_TYPE_ZERO_TOUCH"`)




