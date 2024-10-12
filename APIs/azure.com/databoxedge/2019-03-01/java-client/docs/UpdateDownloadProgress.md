

# UpdateDownloadProgress

Details about the download progress of update.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**downloadPhase** | [**DownloadPhaseEnum**](#DownloadPhaseEnum) | The download phase. |  [optional] [readonly] |
|**numberOfUpdatesDownloaded** | **Integer** | Number of updates downloaded. |  [optional] [readonly] |
|**numberOfUpdatesToDownload** | **Integer** | Number of updates to download. |  [optional] [readonly] |
|**percentComplete** | **Integer** | Percentage of completion. |  [optional] [readonly] |
|**totalBytesDownloaded** | **Double** | Total bytes downloaded. |  [optional] [readonly] |
|**totalBytesToDownload** | **Double** | Total bytes to download. |  [optional] [readonly] |



## Enum: DownloadPhaseEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;Unknown&quot; |
| INITIALIZING | &quot;Initializing&quot; |
| DOWNLOADING | &quot;Downloading&quot; |
| VERIFYING | &quot;Verifying&quot; |



