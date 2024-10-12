

# GoogleChromeManagementV1BatteryInfo

Information about the battery. * This field provides device information, which is static and will not change over time. * Data for this field is controlled via policy: [ReportDevicePowerStatus](https://chromeenterprise.google/policies/#ReportDevicePowerStatus) * Data Collection Frequency: Only at Upload * Default Data Reporting Frequency: 3 hours - Policy Controlled: Yes * Cache: If the device is offline, the collected data is stored locally, and will be reported when the device is next online: No * Reported for affiliated users only: N/A * Granular permission needed: TELEMETRY_API_BATTERY_INFO

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**designCapacity** | **String** | Output only. Design capacity (mAmpere-hours). |  [optional] [readonly] |
|**designMinVoltage** | **Integer** | Output only. Designed minimum output voltage (mV) |  [optional] [readonly] |
|**manufactureDate** | [**GoogleTypeDate**](GoogleTypeDate.md) |  |  [optional] |
|**manufacturer** | **String** | Output only. Battery manufacturer. |  [optional] [readonly] |
|**serialNumber** | **String** | Output only. Battery serial number. |  [optional] [readonly] |
|**technology** | **String** | Output only. Technology of the battery. Example: Li-ion |  [optional] [readonly] |



