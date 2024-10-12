# GooglePlayAndroidDeveloperApi.DeviceSelector

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deviceRam** | [**DeviceRam**](DeviceRam.md) |  | [optional] 
**excludedDeviceIds** | [**[DeviceId]**](DeviceId.md) | Device models excluded by this selector, even if they match all other conditions. | [optional] 
**forbiddenSystemFeatures** | [**[SystemFeature]**](SystemFeature.md) | A device that has any of these system features is excluded by this selector, even if it matches all other conditions. | [optional] 
**includedDeviceIds** | [**[DeviceId]**](DeviceId.md) | Device models included by this selector. | [optional] 
**requiredSystemFeatures** | [**[SystemFeature]**](SystemFeature.md) | A device needs to have all these system features to be included by the selector. | [optional] 


