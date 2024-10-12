# AndroidDeviceProvisioningPartnerApi.Device

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**claims** | [**[DeviceClaim]**](DeviceClaim.md) | Output only. The provisioning claims for a device. Devices claimed for zero-touch enrollment have a claim with the type &#x60;SECTION_TYPE_ZERO_TOUCH&#x60;. Call &#x60;partners.devices.unclaim&#x60; or &#x60;partners.devices.unclaimAsync&#x60; to remove the device from zero-touch enrollment. | [optional] [readonly] 
**configuration** | **String** | Not available to resellers. | [optional] 
**deviceId** | **String** | Output only. The ID of the device. Assigned by the server. | [optional] [readonly] 
**deviceIdentifier** | [**DeviceIdentifier**](DeviceIdentifier.md) |  | [optional] 
**deviceMetadata** | [**DeviceMetadata**](DeviceMetadata.md) |  | [optional] 
**name** | **String** | Output only. The API resource name in the format &#x60;partners/[PARTNER_ID]/devices/[DEVICE_ID]&#x60;. Assigned by the server. | [optional] [readonly] 


