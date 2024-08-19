

# GoogleChromeManagementV1BootPerformanceReport

Boot performance report of a device. * This field is telemetry information and this will change over time as the device is utilized. * Data for this field is controlled via policy: [ReportDeviceBootMode](https://chromeenterprise.google/policies/#ReportDeviceBootMode) * Data Collection Frequency: On every boot up event * Default Data Reporting Frequency: 3 hours - Policy Controlled: Yes * Cache: If the device is offline, the collected data is stored locally, and will be reported when the device is next online: Yes * Reported for affiliated users only: N/A * Granular permission needed: TELEMETRY_API_OS_REPORT

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bootUpDuration** | **String** | Total time to boot up. |  [optional] |
|**bootUpTime** | **String** | The timestamp when power came on. |  [optional] |
|**reportTime** | **String** | Timestamp when the report was collected. |  [optional] |
|**shutdownDuration** | **String** | Total time since shutdown start to power off. |  [optional] |
|**shutdownReason** | [**ShutdownReasonEnum**](#ShutdownReasonEnum) | The shutdown reason. |  [optional] |
|**shutdownTime** | **String** | The timestamp when shutdown. |  [optional] |



## Enum: ShutdownReasonEnum

| Name | Value |
|---- | -----|
| SHUTDOWN_REASON_UNSPECIFIED | &quot;SHUTDOWN_REASON_UNSPECIFIED&quot; |
| USER_REQUEST | &quot;USER_REQUEST&quot; |
| SYSTEM_UPDATE | &quot;SYSTEM_UPDATE&quot; |
| LOW_BATTERY | &quot;LOW_BATTERY&quot; |
| OTHER | &quot;OTHER&quot; |



