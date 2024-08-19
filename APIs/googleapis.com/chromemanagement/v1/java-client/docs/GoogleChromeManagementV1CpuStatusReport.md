

# GoogleChromeManagementV1CpuStatusReport

Provides information about the status of the CPU. * This field is telemetry information and this will change over time as the device is utilized. * Data for this field is controlled via policy: [ReportDeviceCpuInfo](https://chromeenterprise.google/policies/#ReportDeviceCpuInfo) * Data Collection Frequency: Every 10 minutes * Default Data Reporting Frequency: 3 hours - Policy Controlled: Yes * Cache: If the device is offline, the collected data is stored locally, and will be reported when the device is next online: No * Reported for affiliated users only: N/A * Granular permission needed: TELEMETRY_API_CPU_REPORT

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cpuTemperatureInfo** | [**List&lt;GoogleChromeManagementV1CpuTemperatureInfo&gt;**](GoogleChromeManagementV1CpuTemperatureInfo.md) | Output only. CPU temperature sample info per CPU core in Celsius |  [optional] [readonly] |
|**cpuUtilizationPct** | **Integer** | Output only. Sample of CPU utilization (0-100 percent). |  [optional] [readonly] |
|**reportTime** | **String** | Output only. The timestamp in milliseconds representing time at which this report was sampled. |  [optional] [readonly] |
|**sampleFrequency** | **String** | Output only. Frequency the report is sampled. |  [optional] [readonly] |



