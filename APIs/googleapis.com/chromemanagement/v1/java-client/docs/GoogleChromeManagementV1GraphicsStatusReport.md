

# GoogleChromeManagementV1GraphicsStatusReport

Information of the graphics subsystem. * This field is telemetry information and this will change over time as the device is utilized. * Data for this field is controlled via policy: [ReportDeviceGraphicsInfo](https://chromeenterprise.google/policies/#ReportDeviceGraphicsInfo) * Data Collection Frequency: 3 hours. * Default Data Reporting Frequency: 3 hours - Policy Controlled: Yes * Cache: If the device is offline, the collected data is stored locally, and will be reported when the device is next online: No * Reported for affiliated users only: N/A * Granular permission needed: TELEMETRY_API_GRAPHICS_REPORT

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**displays** | [**List&lt;GoogleChromeManagementV1DisplayInfo&gt;**](GoogleChromeManagementV1DisplayInfo.md) | Output only. Information about the displays for the device. |  [optional] [readonly] |
|**reportTime** | **String** | Output only. Time at which the graphics data was reported. |  [optional] [readonly] |



