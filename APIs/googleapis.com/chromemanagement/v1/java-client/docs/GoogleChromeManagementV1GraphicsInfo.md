

# GoogleChromeManagementV1GraphicsInfo

Information of the graphics subsystem. * This field provides device information, which is static and will not change over time. * Data for this field is controlled via policy: [ReportDeviceGraphicsStatus](https://chromeenterprise.google/policies/#ReportDeviceGraphicsStatus) * Data Collection Frequency: Only at Upload * Default Data Reporting Frequency: 3 hours - Policy Controlled: Yes * Cache: If the device is offline, the collected data is stored locally, and will be reported when the device is next online: No * Reported for affiliated users only: N/A * Granular permission needed: TELEMETRY_API_GRAPHICS_INFO

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adapterInfo** | [**GoogleChromeManagementV1GraphicsAdapterInfo**](GoogleChromeManagementV1GraphicsAdapterInfo.md) |  |  [optional] |
|**displayDevices** | [**List&lt;GoogleChromeManagementV1DisplayDevice&gt;**](GoogleChromeManagementV1DisplayDevice.md) | Output only. Information about the display(s) of the device. |  [optional] [readonly] |
|**eprivacySupported** | **Boolean** | Output only. Is ePrivacy screen supported or not. |  [optional] [readonly] |
|**touchScreenInfo** | [**GoogleChromeManagementV1TouchScreenInfo**](GoogleChromeManagementV1TouchScreenInfo.md) |  |  [optional] |



