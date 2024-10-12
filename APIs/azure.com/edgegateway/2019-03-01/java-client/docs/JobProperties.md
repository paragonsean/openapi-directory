

# JobProperties

The properties for the job.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**currentStage** | [**CurrentStageEnum**](#CurrentStageEnum) | Current stage of the update operation. |  [optional] [readonly] |
|**downloadProgress** | [**UpdateDownloadProgress**](UpdateDownloadProgress.md) |  |  [optional] |
|**errorManifestFile** | **String** | Local share/remote container relative path to the error manifest file of the refresh. |  [optional] [readonly] |
|**folder** | **String** | If only subfolders need to be refreshed, then the subfolder path inside the share. (The path is empty if there are no subfolders.) |  [optional] |
|**installProgress** | [**UpdateInstallProgress**](UpdateInstallProgress.md) |  |  [optional] |
|**jobType** | [**JobTypeEnum**](#JobTypeEnum) | The type of the job. |  [optional] [readonly] |
|**shareId** | **String** | ARM ID of the share that was refreshed. |  [optional] [readonly] |
|**totalRefreshErrors** | **Integer** | Total number of errors encountered during the refresh process. |  [optional] [readonly] |



## Enum: CurrentStageEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;Unknown&quot; |
| INITIAL | &quot;Initial&quot; |
| SCAN_STARTED | &quot;ScanStarted&quot; |
| SCAN_COMPLETE | &quot;ScanComplete&quot; |
| SCAN_FAILED | &quot;ScanFailed&quot; |
| DOWNLOAD_STARTED | &quot;DownloadStarted&quot; |
| DOWNLOAD_COMPLETE | &quot;DownloadComplete&quot; |
| DOWNLOAD_FAILED | &quot;DownloadFailed&quot; |
| INSTALL_STARTED | &quot;InstallStarted&quot; |
| INSTALL_COMPLETE | &quot;InstallComplete&quot; |
| INSTALL_FAILED | &quot;InstallFailed&quot; |
| REBOOT_INITIATED | &quot;RebootInitiated&quot; |
| SUCCESS | &quot;Success&quot; |
| FAILURE | &quot;Failure&quot; |
| RESCAN_STARTED | &quot;RescanStarted&quot; |
| RESCAN_COMPLETE | &quot;RescanComplete&quot; |
| RESCAN_FAILED | &quot;RescanFailed&quot; |



## Enum: JobTypeEnum

| Name | Value |
|---- | -----|
| INVALID | &quot;Invalid&quot; |
| SCAN_FOR_UPDATES | &quot;ScanForUpdates&quot; |
| DOWNLOAD_UPDATES | &quot;DownloadUpdates&quot; |
| INSTALL_UPDATES | &quot;InstallUpdates&quot; |
| REFRESH_SHARE | &quot;RefreshShare&quot; |



