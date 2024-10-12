

# UpdatesProperties

Properties of the update profile

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**deviceLastScannedTime** | **OffsetDateTime** | The last time when the device did an update scan. |  [optional] |
|**deviceVersion** | **String** | The current Device version. |  [optional] |
|**inProgressDownloadJobId** | **String** | If a download is in progress, this field contains the JobId of that particular download job |  [optional] |
|**inProgressDownloadJobStartedTime** | **OffsetDateTime** | The time when the currently running download (if any) started |  [optional] |
|**inProgressInstallJobId** | **String** | If an install is in progress, this field contains the JobId of that particular install job |  [optional] |
|**inProgressInstallJobStartedTime** | **OffsetDateTime** | The time when the currently running install (if any) started |  [optional] |
|**inProgressScanStartedTime** | **OffsetDateTime** | The time when the currently running scan (if any) started |  [optional] |
|**lastCompletedDownloadJobTime** | **OffsetDateTime** | The time when the last Download job was completed (success|cancelled|failed) on the device. |  [optional] |
|**lastCompletedInstallJobTime** | **OffsetDateTime** | The time when the last Install job was completed (success|cancelled|failed) on the device. |  [optional] |
|**lastCompletedScanTime** | **OffsetDateTime** | The time when the last scan job was completed (success|cancelled|failed) on the device. |  [optional] |
|**rebootRequiredForInstall** | **Boolean** | Set to true if RegularUpdatesAvailable is true and if at least one of the updateItems detected has needs a reboot to install. |  [optional] |
|**regularUpdatesAvailable** | **Boolean** | Set to true if regular updates were detected for the current version of the device. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The current update operation. |  [optional] |
|**totalItemsPendingForDownload** | **Integer** | The total number of items pending for download. |  [optional] |
|**totalItemsPendingForInstall** | **Integer** | The total number of items pending for install. |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| IDLE | &quot;Idle&quot; |
| SCANNING | &quot;Scanning&quot; |
| DOWNLOADING | &quot;Downloading&quot; |
| INSTALLING | &quot;Installing&quot; |



