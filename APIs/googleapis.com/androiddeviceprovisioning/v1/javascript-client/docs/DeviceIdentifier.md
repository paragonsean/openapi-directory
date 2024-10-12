# AndroidDeviceProvisioningPartnerApi.DeviceIdentifier

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chromeOsAttestedDeviceId** | **String** | An identifier provided by OEMs, carried through the production and sales process. Only applicable to Chrome OS devices. | [optional] 
**deviceType** | **String** | The type of the device | [optional] 
**imei** | **String** | The device’s IMEI number. Validated on input. | [optional] 
**manufacturer** | **String** | The device manufacturer’s name. Matches the device&#39;s built-in value returned from &#x60;android.os.Build.MANUFACTURER&#x60;. Allowed values are listed in [Android manufacturers](/zero-touch/resources/manufacturer-names#manufacturers-names). | [optional] 
**meid** | **String** | The device’s MEID number. | [optional] 
**model** | **String** | The device model&#39;s name. Allowed values are listed in [Android models](/zero-touch/resources/manufacturer-names#model-names) and [Chrome OS models](https://support.google.com/chrome/a/answer/10130175#identify_compatible). | [optional] 
**serialNumber** | **String** | The manufacturer&#39;s serial number for the device. This value might not be unique across different device models. | [optional] 



## Enum: DeviceTypeEnum


* `UNSPECIFIED` (value: `"DEVICE_TYPE_UNSPECIFIED"`)

* `ANDROID` (value: `"DEVICE_TYPE_ANDROID"`)

* `CHROME_OS` (value: `"DEVICE_TYPE_CHROME_OS"`)




