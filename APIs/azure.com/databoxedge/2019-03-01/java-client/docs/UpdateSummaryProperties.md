

# UpdateSummaryProperties

The device update information summary.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**deviceLastScannedDateTime** | **OffsetDateTime** | The last time when a scan was done on the device. |  [optional] |
|**deviceVersionNumber** | **String** | The current version of the device in format: 1.2.17312.13.\&quot;, |  [optional] |
|**friendlyDeviceVersionName** | **String** | The current version of the device in text format. |  [optional] |
|**inProgressDownloadJobId** | **String** | The job ID of the download job in progress. |  [optional] [readonly] |
|**inProgressDownloadJobStartedDateTime** | **OffsetDateTime** | The time when the currently running download (if any) started. |  [optional] [readonly] |
|**inProgressInstallJobId** | **String** | The job ID of the install job in progress. |  [optional] [readonly] |
|**inProgressInstallJobStartedDateTime** | **OffsetDateTime** | The time when the currently running install (if any) started. |  [optional] [readonly] |
|**lastCompletedDownloadJobDateTime** | **OffsetDateTime** | The time when the last Download job was completed (success/cancelled/failed) on the appliance. |  [optional] [readonly] |
|**lastCompletedInstallJobDateTime** | **OffsetDateTime** | The time when the last Install job was completed (success/cancelled/failed) on the appliance. |  [optional] [readonly] |
|**lastCompletedScanJobDateTime** | **OffsetDateTime** | The time when the last scan job was completed (success/cancelled/failed) on the appliance. |  [optional] |
|**ongoingUpdateOperation** | [**OngoingUpdateOperationEnum**](#OngoingUpdateOperationEnum) | The current update operation. |  [optional] [readonly] |
|**rebootBehavior** | [**RebootBehaviorEnum**](#RebootBehaviorEnum) | Indicates if updates are available and at least one of the updates needs a reboot. |  [optional] [readonly] |
|**totalNumberOfUpdatesAvailable** | **Integer** | The number of updates available for the current device version as per the last device scan. |  [optional] [readonly] |
|**totalNumberOfUpdatesPendingDownload** | **Integer** | The total number of items pending download. |  [optional] [readonly] |
|**totalNumberOfUpdatesPendingInstall** | **Integer** | The total number of items pending install. |  [optional] [readonly] |
|**totalUpdateSizeInBytes** | **Double** | The total size of updates available for download in bytes. |  [optional] [readonly] |
|**updateTitles** | **List&lt;String&gt;** | The list of updates available for install. |  [optional] [readonly] |



## Enum: OngoingUpdateOperationEnum

| Name | Value |
|---- | -----|
| NONE | &quot;None&quot; |
| SCAN | &quot;Scan&quot; |
| DOWNLOAD | &quot;Download&quot; |
| INSTALL | &quot;Install&quot; |



## Enum: RebootBehaviorEnum

| Name | Value |
|---- | -----|
| NEVER_REBOOTS | &quot;NeverReboots&quot; |
| REQUIRES_REBOOT | &quot;RequiresReboot&quot; |
| REQUEST_REBOOT | &quot;RequestReboot&quot; |



