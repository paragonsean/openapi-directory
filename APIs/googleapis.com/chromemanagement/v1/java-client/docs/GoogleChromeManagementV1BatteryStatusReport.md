

# GoogleChromeManagementV1BatteryStatusReport

Status data for battery. * This field is telemetry information and this will change over time as the device is utilized. * Data for this field is controlled via policy: [ReportDevicePowerStatus](https://chromeenterprise.google/policies/#ReportDevicePowerStatus) * Data Collection Frequency: Only at Upload * Default Data Reporting Frequency: 3 hours - Policy Controlled: Yes * Cache: If the device is offline, the collected data is stored locally, and will be reported when the device is next online: No * Reported for affiliated users only: N/A * Granular permission needed: TELEMETRY_API_BATTERY_REPORT

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**batteryHealth** | [**BatteryHealthEnum**](#BatteryHealthEnum) | Output only. Battery health. |  [optional] [readonly] |
|**cycleCount** | **Integer** | Output only. Cycle count. |  [optional] [readonly] |
|**fullChargeCapacity** | **String** | Output only. Full charge capacity (mAmpere-hours). |  [optional] [readonly] |
|**reportTime** | **String** | Output only. Timestamp of when the sample was collected on device |  [optional] [readonly] |
|**sample** | [**List&lt;GoogleChromeManagementV1BatterySampleReport&gt;**](GoogleChromeManagementV1BatterySampleReport.md) | Output only. Sampling data for the battery sorted in a decreasing order of report_time. |  [optional] [readonly] |
|**serialNumber** | **String** | Output only. Battery serial number. |  [optional] [readonly] |



## Enum: BatteryHealthEnum

| Name | Value |
|---- | -----|
| HEALTH_UNSPECIFIED | &quot;BATTERY_HEALTH_UNSPECIFIED&quot; |
| HEALTH_NORMAL | &quot;BATTERY_HEALTH_NORMAL&quot; |
| REPLACE_SOON | &quot;BATTERY_REPLACE_SOON&quot; |
| REPLACE_NOW | &quot;BATTERY_REPLACE_NOW&quot; |



