# CloudTestingApi.IosModel

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deviceCapabilities** | **[String]** | Device capabilities. Copied from https://developer.apple.com/library/archive/documentation/DeviceInformation/Reference/iOSDeviceCompatibility/DeviceCompatibilityMatrix/DeviceCompatibilityMatrix.html | [optional] 
**formFactor** | **String** | Whether this device is a phone, tablet, wearable, etc. | [optional] 
**id** | **String** | The unique opaque id for this model. Use this for invoking the TestExecutionService. | [optional] 
**name** | **String** | The human-readable name for this device model. Examples: \&quot;iPhone 4s\&quot;, \&quot;iPad Mini 2\&quot;. | [optional] 
**perVersionInfo** | [**[PerIosVersionInfo]**](PerIosVersionInfo.md) | Version-specific information of an iOS model. | [optional] 
**screenDensity** | **Number** | Screen density in DPI. | [optional] 
**screenX** | **Number** | Screen size in the horizontal (X) dimension measured in pixels. | [optional] 
**screenY** | **Number** | Screen size in the vertical (Y) dimension measured in pixels. | [optional] 
**supportedVersionIds** | **[String]** | The set of iOS major software versions this device supports. | [optional] 
**tags** | **[String]** | Tags for this dimension. Examples: \&quot;default\&quot;, \&quot;preview\&quot;, \&quot;deprecated\&quot;. | [optional] 



## Enum: FormFactorEnum


* `DEVICE_FORM_FACTOR_UNSPECIFIED` (value: `"DEVICE_FORM_FACTOR_UNSPECIFIED"`)

* `PHONE` (value: `"PHONE"`)

* `TABLET` (value: `"TABLET"`)

* `WEARABLE` (value: `"WEARABLE"`)




