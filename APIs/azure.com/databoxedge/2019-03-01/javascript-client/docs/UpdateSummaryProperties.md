# DataBoxEdgeManagementClient.UpdateSummaryProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deviceLastScannedDateTime** | **Date** | The last time when a scan was done on the device. | [optional] 
**deviceVersionNumber** | **String** | The current version of the device in format: 1.2.17312.13.\&quot;, | [optional] 
**friendlyDeviceVersionName** | **String** | The current version of the device in text format. | [optional] 
**inProgressDownloadJobId** | **String** | The job ID of the download job in progress. | [optional] [readonly] 
**inProgressDownloadJobStartedDateTime** | **Date** | The time when the currently running download (if any) started. | [optional] [readonly] 
**inProgressInstallJobId** | **String** | The job ID of the install job in progress. | [optional] [readonly] 
**inProgressInstallJobStartedDateTime** | **Date** | The time when the currently running install (if any) started. | [optional] [readonly] 
**lastCompletedDownloadJobDateTime** | **Date** | The time when the last Download job was completed (success/cancelled/failed) on the appliance. | [optional] [readonly] 
**lastCompletedInstallJobDateTime** | **Date** | The time when the last Install job was completed (success/cancelled/failed) on the appliance. | [optional] [readonly] 
**lastCompletedScanJobDateTime** | **Date** | The time when the last scan job was completed (success/cancelled/failed) on the appliance. | [optional] 
**ongoingUpdateOperation** | **String** | The current update operation. | [optional] [readonly] 
**rebootBehavior** | **String** | Indicates if updates are available and at least one of the updates needs a reboot. | [optional] [readonly] 
**totalNumberOfUpdatesAvailable** | **Number** | The number of updates available for the current device version as per the last device scan. | [optional] [readonly] 
**totalNumberOfUpdatesPendingDownload** | **Number** | The total number of items pending download. | [optional] [readonly] 
**totalNumberOfUpdatesPendingInstall** | **Number** | The total number of items pending install. | [optional] [readonly] 
**totalUpdateSizeInBytes** | **Number** | The total size of updates available for download in bytes. | [optional] [readonly] 
**updateTitles** | **[String]** | The list of updates available for install. | [optional] [readonly] 



## Enum: OngoingUpdateOperationEnum


* `None` (value: `"None"`)

* `Scan` (value: `"Scan"`)

* `Download` (value: `"Download"`)

* `Install` (value: `"Install"`)





## Enum: RebootBehaviorEnum


* `NeverReboots` (value: `"NeverReboots"`)

* `RequiresReboot` (value: `"RequiresReboot"`)

* `RequestReboot` (value: `"RequestReboot"`)




