

# IosModel

A description of an iOS device tests may be run on.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**deviceCapabilities** | **List&lt;String&gt;** | Device capabilities. Copied from https://developer.apple.com/library/archive/documentation/DeviceInformation/Reference/iOSDeviceCompatibility/DeviceCompatibilityMatrix/DeviceCompatibilityMatrix.html |  [optional] |
|**formFactor** | [**FormFactorEnum**](#FormFactorEnum) | Whether this device is a phone, tablet, wearable, etc. |  [optional] |
|**id** | **String** | The unique opaque id for this model. Use this for invoking the TestExecutionService. |  [optional] |
|**name** | **String** | The human-readable name for this device model. Examples: \&quot;iPhone 4s\&quot;, \&quot;iPad Mini 2\&quot;. |  [optional] |
|**perVersionInfo** | [**List&lt;PerIosVersionInfo&gt;**](PerIosVersionInfo.md) | Version-specific information of an iOS model. |  [optional] |
|**screenDensity** | **Integer** | Screen density in DPI. |  [optional] |
|**screenX** | **Integer** | Screen size in the horizontal (X) dimension measured in pixels. |  [optional] |
|**screenY** | **Integer** | Screen size in the vertical (Y) dimension measured in pixels. |  [optional] |
|**supportedVersionIds** | **List&lt;String&gt;** | The set of iOS major software versions this device supports. |  [optional] |
|**tags** | **List&lt;String&gt;** | Tags for this dimension. Examples: \&quot;default\&quot;, \&quot;preview\&quot;, \&quot;deprecated\&quot;. |  [optional] |



## Enum: FormFactorEnum

| Name | Value |
|---- | -----|
| DEVICE_FORM_FACTOR_UNSPECIFIED | &quot;DEVICE_FORM_FACTOR_UNSPECIFIED&quot; |
| PHONE | &quot;PHONE&quot; |
| TABLET | &quot;TABLET&quot; |
| WEARABLE | &quot;WEARABLE&quot; |



