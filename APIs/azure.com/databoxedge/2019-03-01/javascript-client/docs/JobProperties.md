# DataBoxEdgeManagementClient.JobProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currentStage** | **String** | Current stage of the update operation. | [optional] [readonly] 
**downloadProgress** | [**UpdateDownloadProgress**](UpdateDownloadProgress.md) |  | [optional] 
**errorManifestFile** | **String** | Local share/remote container relative path to the error manifest file of the refresh. | [optional] [readonly] 
**folder** | **String** | If only subfolders need to be refreshed, then the subfolder path inside the share. (The path is empty if there are no subfolders.) | [optional] 
**installProgress** | [**UpdateInstallProgress**](UpdateInstallProgress.md) |  | [optional] 
**jobType** | **String** | The type of the job. | [optional] [readonly] 
**shareId** | **String** | ARM ID of the share that was refreshed. | [optional] [readonly] 
**totalRefreshErrors** | **Number** | Total number of errors encountered during the refresh process. | [optional] [readonly] 



## Enum: CurrentStageEnum


* `Unknown` (value: `"Unknown"`)

* `Initial` (value: `"Initial"`)

* `ScanStarted` (value: `"ScanStarted"`)

* `ScanComplete` (value: `"ScanComplete"`)

* `ScanFailed` (value: `"ScanFailed"`)

* `DownloadStarted` (value: `"DownloadStarted"`)

* `DownloadComplete` (value: `"DownloadComplete"`)

* `DownloadFailed` (value: `"DownloadFailed"`)

* `InstallStarted` (value: `"InstallStarted"`)

* `InstallComplete` (value: `"InstallComplete"`)

* `InstallFailed` (value: `"InstallFailed"`)

* `RebootInitiated` (value: `"RebootInitiated"`)

* `Success` (value: `"Success"`)

* `Failure` (value: `"Failure"`)

* `RescanStarted` (value: `"RescanStarted"`)

* `RescanComplete` (value: `"RescanComplete"`)

* `RescanFailed` (value: `"RescanFailed"`)





## Enum: JobTypeEnum


* `Invalid` (value: `"Invalid"`)

* `ScanForUpdates` (value: `"ScanForUpdates"`)

* `DownloadUpdates` (value: `"DownloadUpdates"`)

* `InstallUpdates` (value: `"InstallUpdates"`)

* `RefreshShare` (value: `"RefreshShare"`)




