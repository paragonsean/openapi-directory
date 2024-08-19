# ChromeManagementApi.GoogleChromeManagementV1OsUpdateStatus

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lastRebootTime** | **String** | Output only. Timestamp of the last reboot. | [optional] [readonly] 
**lastUpdateCheckTime** | **String** | Output only. Timestamp of the last update check. | [optional] [readonly] 
**lastUpdateTime** | **String** | Output only. Timestamp of the last successful update. | [optional] [readonly] 
**newPlatformVersion** | **String** | Output only. New platform version of the os image being downloaded and applied. It is only set when update status is OS_IMAGE_DOWNLOAD_IN_PROGRESS or OS_UPDATE_NEED_REBOOT. Note this could be a dummy \&quot;0.0.0.0\&quot; for OS_UPDATE_NEED_REBOOT status for some edge cases, e.g. update engine is restarted without a reboot. | [optional] [readonly] 
**newRequestedPlatformVersion** | **String** | Output only. New requested platform version from the pending updated kiosk app. | [optional] [readonly] 
**updateState** | **String** | Output only. Current state of the os update. | [optional] [readonly] 



## Enum: UpdateStateEnum


* `UPDATE_STATE_UNSPECIFIED` (value: `"UPDATE_STATE_UNSPECIFIED"`)

* `OS_IMAGE_DOWNLOAD_NOT_STARTED` (value: `"OS_IMAGE_DOWNLOAD_NOT_STARTED"`)

* `OS_IMAGE_DOWNLOAD_IN_PROGRESS` (value: `"OS_IMAGE_DOWNLOAD_IN_PROGRESS"`)

* `OS_UPDATE_NEED_REBOOT` (value: `"OS_UPDATE_NEED_REBOOT"`)




