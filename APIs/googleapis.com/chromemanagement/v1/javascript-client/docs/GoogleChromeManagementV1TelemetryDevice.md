# ChromeManagementApi.GoogleChromeManagementV1TelemetryDevice

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audioStatusReport** | [**[GoogleChromeManagementV1AudioStatusReport]**](GoogleChromeManagementV1AudioStatusReport.md) | Output only. Audio reports collected periodically sorted in a decreasing order of report_time. | [optional] [readonly] 
**batteryInfo** | [**[GoogleChromeManagementV1BatteryInfo]**](GoogleChromeManagementV1BatteryInfo.md) | Output only. Information on battery specs for the device. | [optional] [readonly] 
**batteryStatusReport** | [**[GoogleChromeManagementV1BatteryStatusReport]**](GoogleChromeManagementV1BatteryStatusReport.md) | Output only. Battery reports collected periodically. | [optional] [readonly] 
**bootPerformanceReport** | [**[GoogleChromeManagementV1BootPerformanceReport]**](GoogleChromeManagementV1BootPerformanceReport.md) | Output only. Boot performance reports of the device. | [optional] [readonly] 
**cpuInfo** | [**[GoogleChromeManagementV1CpuInfo]**](GoogleChromeManagementV1CpuInfo.md) | Output only. Information regarding CPU specs for the device. | [optional] [readonly] 
**cpuStatusReport** | [**[GoogleChromeManagementV1CpuStatusReport]**](GoogleChromeManagementV1CpuStatusReport.md) | Output only. CPU status reports collected periodically sorted in a decreasing order of report_time. | [optional] [readonly] 
**customer** | **String** | Output only. Google Workspace Customer whose enterprise enrolled the device. | [optional] [readonly] 
**deviceId** | **String** | Output only. The unique Directory API ID of the device. This value is the same as the Admin Console&#39;s Directory API ID in the ChromeOS Devices tab | [optional] [readonly] 
**graphicsInfo** | [**GoogleChromeManagementV1GraphicsInfo**](GoogleChromeManagementV1GraphicsInfo.md) |  | [optional] 
**graphicsStatusReport** | [**[GoogleChromeManagementV1GraphicsStatusReport]**](GoogleChromeManagementV1GraphicsStatusReport.md) | Output only. Graphics reports collected periodically. | [optional] [readonly] 
**heartbeatStatusReport** | [**[GoogleChromeManagementV1HeartbeatStatusReport]**](GoogleChromeManagementV1HeartbeatStatusReport.md) | Output only. Heartbeat status report containing timestamps periodically sorted in decreasing order of report_time | [optional] [readonly] 
**kioskAppStatusReport** | [**[GoogleChromeManagementV1KioskAppStatusReport]**](GoogleChromeManagementV1KioskAppStatusReport.md) | Output only. Kiosk app status report for the kiosk device | [optional] [readonly] 
**memoryInfo** | [**GoogleChromeManagementV1MemoryInfo**](GoogleChromeManagementV1MemoryInfo.md) |  | [optional] 
**memoryStatusReport** | [**[GoogleChromeManagementV1MemoryStatusReport]**](GoogleChromeManagementV1MemoryStatusReport.md) | Output only. Memory status reports collected periodically sorted decreasing by report_time. | [optional] [readonly] 
**name** | **String** | Output only. Resource name of the device. | [optional] [readonly] 
**networkBandwidthReport** | [**[GoogleChromeManagementV1NetworkBandwidthReport]**](GoogleChromeManagementV1NetworkBandwidthReport.md) | Output only. Network bandwidth reports collected periodically sorted in a decreasing order of report_time. | [optional] [readonly] 
**networkDiagnosticsReport** | [**[GoogleChromeManagementV1NetworkDiagnosticsReport]**](GoogleChromeManagementV1NetworkDiagnosticsReport.md) | Output only. Network diagnostics collected periodically. | [optional] [readonly] 
**networkInfo** | [**GoogleChromeManagementV1NetworkInfo**](GoogleChromeManagementV1NetworkInfo.md) |  | [optional] 
**networkStatusReport** | [**[GoogleChromeManagementV1NetworkStatusReport]**](GoogleChromeManagementV1NetworkStatusReport.md) | Output only. Network specs collected periodically. | [optional] [readonly] 
**orgUnitId** | **String** | Output only. Organization unit ID of the device. | [optional] [readonly] 
**osUpdateStatus** | [**[GoogleChromeManagementV1OsUpdateStatus]**](GoogleChromeManagementV1OsUpdateStatus.md) | Output only. Contains relevant information regarding ChromeOS update status. | [optional] [readonly] 
**peripheralsReport** | [**[GoogleChromeManagementV1PeripheralsReport]**](GoogleChromeManagementV1PeripheralsReport.md) | Output only. Peripherals reports collected periodically sorted in a decreasing order of report_time. | [optional] [readonly] 
**runtimeCountersReport** | [**[GoogleChromeManagementV1RuntimeCountersReport]**](GoogleChromeManagementV1RuntimeCountersReport.md) | Output only. Runtime counters reports collected device lifetime runtime, as well as the counts of S0-&gt;S3, S0-&gt;S4, and S0-&gt;S5 transitions, meaning entering into sleep, hibernation, and power-off states | [optional] [readonly] 
**serialNumber** | **String** | Output only. Device serial number. This value is the same as the Admin Console&#39;s Serial Number in the ChromeOS Devices tab. | [optional] [readonly] 
**storageInfo** | [**GoogleChromeManagementV1StorageInfo**](GoogleChromeManagementV1StorageInfo.md) |  | [optional] 
**storageStatusReport** | [**[GoogleChromeManagementV1StorageStatusReport]**](GoogleChromeManagementV1StorageStatusReport.md) | Output only. Storage reports collected periodically. | [optional] [readonly] 
**thunderboltInfo** | [**[GoogleChromeManagementV1ThunderboltInfo]**](GoogleChromeManagementV1ThunderboltInfo.md) | Output only. Information on Thunderbolt bus. | [optional] [readonly] 


