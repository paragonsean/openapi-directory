

# GoogleChromeManagementV1StorageInfo

Status data for storage. * This field is telemetry information and this will change over time as the device is utilized. * Data for this field is controlled via policy: [ReportDeviceStorageStatus](https://chromeenterprise.google/policies/#ReportDeviceStorageStatus) * Data Collection Frequency: Only at Upload * Default Data Reporting Frequency: 3 hours - Policy Controlled: Yes * Cache: If the device is offline, the collected data is stored locally, and will be reported when the device is next online: No * Reported for affiliated users only: N/A * Granular permission needed: TELEMETRY_API_STORAGE_INFO

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**availableDiskBytes** | **String** | The available space for user data storage in the device in bytes. |  [optional] |
|**totalDiskBytes** | **String** | The total space for user data storage in the device in bytes. |  [optional] |
|**volume** | [**List&lt;GoogleChromeManagementV1StorageInfoDiskVolume&gt;**](GoogleChromeManagementV1StorageInfoDiskVolume.md) | Information for disk volumes |  [optional] |



