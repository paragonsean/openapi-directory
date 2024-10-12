

# DeviceSelector

Selector for a device group. A selector consists of a set of conditions on the device that should all match (logical AND) to determine a device group eligibility. For instance, if a selector specifies RAM conditions, device model inclusion and device model exclusion, a device is considered to match if: device matches RAM conditions AND device matches one of the included device models AND device doesn't match excluded device models

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**deviceRam** | [**DeviceRam**](DeviceRam.md) |  |  [optional] |
|**excludedDeviceIds** | [**List&lt;DeviceId&gt;**](DeviceId.md) | Device models excluded by this selector, even if they match all other conditions. |  [optional] |
|**forbiddenSystemFeatures** | [**List&lt;SystemFeature&gt;**](SystemFeature.md) | A device that has any of these system features is excluded by this selector, even if it matches all other conditions. |  [optional] |
|**includedDeviceIds** | [**List&lt;DeviceId&gt;**](DeviceId.md) | Device models included by this selector. |  [optional] |
|**requiredSystemFeatures** | [**List&lt;SystemFeature&gt;**](SystemFeature.md) | A device needs to have all these system features to be included by the selector. |  [optional] |



