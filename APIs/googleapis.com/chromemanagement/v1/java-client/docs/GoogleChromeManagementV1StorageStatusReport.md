

# GoogleChromeManagementV1StorageStatusReport

Status data for storage. * This field is telemetry information and this will change over time as the device is utilized. * Data for this field is controlled via policy: [ReportDeviceStorageStatus](https://chromeenterprise.google/policies/#ReportDeviceStorageStatus) * Data Collection Frequency: Only at Upload * Default Data Reporting Frequency: 3 hours - Policy Controlled: Yes * Cache: If the device is offline, the collected data is stored locally, and will be reported when the device is next online: No * Reported for affiliated users only: N/A * Granular permission needed: TELEMETRY_API_STORAGE_REPORT

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**disk** | [**List&lt;GoogleChromeManagementV1DiskInfo&gt;**](GoogleChromeManagementV1DiskInfo.md) | Output only. Reports on disk. |  [optional] [readonly] |
|**reportTime** | **String** | Output only. Timestamp of when the sample was collected on device |  [optional] [readonly] |



