

# GoogleChromeManagementV1MemoryStatusReport

Contains samples of memory status reports. * This field is telemetry information and this will change over time as the device is utilized. * Data for this field is controlled via policy: [ReportDeviceMemoryInfo](https://chromeenterprise.google/policies/#ReportDeviceMemoryInfo) * Data Collection Frequency: Only at upload, SystemRamFreeByes is collected every 10 minutes * Default Data Reporting Frequency: Every 3 hours - Policy Controlled: Yes * Cache: If the device is offline, the collected data is stored locally, and will be reported when the device is next online: No * Reported for affiliated users only: N/A * Granular permission needed: TELEMETRY_API_MEMORY_REPORT

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**pageFaults** | **Integer** | Output only. Number of page faults during this collection |  [optional] [readonly] |
|**reportTime** | **String** | Output only. The timestamp in milliseconds representing time at which this report was sampled. |  [optional] [readonly] |
|**sampleFrequency** | **String** | Output only. Frequency the report is sampled. |  [optional] [readonly] |
|**systemRamFreeBytes** | **String** | Output only. Amount of free RAM in bytes (unreliable due to Garbage Collection). |  [optional] [readonly] |



