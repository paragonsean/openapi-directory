

# GoogleChromeManagementV1TelemetryUserDevice

Telemetry data collected for a managed user and device. * Granular permission needed: TELEMETRY_API_DEVICE

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**audioStatusReport** | [**List&lt;GoogleChromeManagementV1AudioStatusReport&gt;**](GoogleChromeManagementV1AudioStatusReport.md) | Output only. Audio reports collected periodically sorted in a decreasing order of report_time. |  [optional] [readonly] |
|**deviceActivityReport** | [**List&lt;GoogleChromeManagementV1DeviceActivityReport&gt;**](GoogleChromeManagementV1DeviceActivityReport.md) | Output only. Device activity reports collected periodically sorted in a decreasing order of report_time. |  [optional] [readonly] |
|**deviceId** | **String** | The unique Directory API ID of the device. This value is the same as the Admin Console&#39;s Directory API ID in the ChromeOS Devices tab. |  [optional] |
|**networkBandwidthReport** | [**List&lt;GoogleChromeManagementV1NetworkBandwidthReport&gt;**](GoogleChromeManagementV1NetworkBandwidthReport.md) | Output only. Network bandwidth reports collected periodically sorted in a decreasing order of report_time. |  [optional] [readonly] |
|**peripheralsReport** | [**List&lt;GoogleChromeManagementV1PeripheralsReport&gt;**](GoogleChromeManagementV1PeripheralsReport.md) | Output only. Peripherals reports collected periodically sorted in a decreasing order of report_time. |  [optional] [readonly] |



