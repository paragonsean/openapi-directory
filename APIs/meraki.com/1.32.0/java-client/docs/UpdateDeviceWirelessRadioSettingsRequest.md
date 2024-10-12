

# UpdateDeviceWirelessRadioSettingsRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**fiveGhzSettings** | [**UpdateDeviceWirelessRadioSettingsRequestFiveGhzSettings**](UpdateDeviceWirelessRadioSettingsRequestFiveGhzSettings.md) |  |  [optional] |
|**rfProfileId** | **String** | The ID of an RF profile to assign to the device. If the value of this parameter is null, the appropriate basic RF profile (indoor or outdoor) will be assigned to the device. Assigning an RF profile will clear ALL manually configured overrides on the device (channel width, channel, power). |  [optional] |
|**twoFourGhzSettings** | [**UpdateDeviceWirelessRadioSettingsRequestTwoFourGhzSettings**](UpdateDeviceWirelessRadioSettingsRequestTwoFourGhzSettings.md) |  |  [optional] |



