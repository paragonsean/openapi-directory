

# GoogleChromeManagementV1OsUpdateStatus

Contains information regarding the current OS update status. * This field is telemetry information and this will change over time as the device is utilized. * Data for this field is controlled via policy: [ReportDeviceOsUpdateStatus](https://chromeenterprise.google/policies/#ReportDeviceOsUpdateStatus) * Data Collection Frequency: Only at Upload * Default Data Reporting Frequency: 3 hours - Policy Controlled: Yes * Cache: If the device is offline, the collected data is stored locally, and will be reported when the device is next online: No * Reported for affiliated users only: N/A * Granular permission needed: TELEMETRY_API_OS_REPORT

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**lastRebootTime** | **String** | Output only. Timestamp of the last reboot. |  [optional] [readonly] |
|**lastUpdateCheckTime** | **String** | Output only. Timestamp of the last update check. |  [optional] [readonly] |
|**lastUpdateTime** | **String** | Output only. Timestamp of the last successful update. |  [optional] [readonly] |
|**newPlatformVersion** | **String** | Output only. New platform version of the os image being downloaded and applied. It is only set when update status is OS_IMAGE_DOWNLOAD_IN_PROGRESS or OS_UPDATE_NEED_REBOOT. Note this could be a dummy \&quot;0.0.0.0\&quot; for OS_UPDATE_NEED_REBOOT status for some edge cases, e.g. update engine is restarted without a reboot. |  [optional] [readonly] |
|**newRequestedPlatformVersion** | **String** | Output only. New requested platform version from the pending updated kiosk app. |  [optional] [readonly] |
|**updateState** | [**UpdateStateEnum**](#UpdateStateEnum) | Output only. Current state of the os update. |  [optional] [readonly] |



## Enum: UpdateStateEnum

| Name | Value |
|---- | -----|
| UPDATE_STATE_UNSPECIFIED | &quot;UPDATE_STATE_UNSPECIFIED&quot; |
| OS_IMAGE_DOWNLOAD_NOT_STARTED | &quot;OS_IMAGE_DOWNLOAD_NOT_STARTED&quot; |
| OS_IMAGE_DOWNLOAD_IN_PROGRESS | &quot;OS_IMAGE_DOWNLOAD_IN_PROGRESS&quot; |
| OS_UPDATE_NEED_REBOOT | &quot;OS_UPDATE_NEED_REBOOT&quot; |



