

# UpdateDownloadProgress

details available during the download

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**downloadPhase** | [**DownloadPhaseEnum**](#DownloadPhaseEnum) | The download phase. |  [optional] |
|**numberOfUpdatesDownloaded** | **Integer** | Number of updates downloaded. |  [optional] |
|**numberOfUpdatesToDownload** | **Integer** | Number of updates to download. |  [optional] |
|**percentComplete** | **Integer** | Percentage of completion. |  [optional] |
|**totalBytesDownloaded** | **Double** | Total bytes downloaded. |  [optional] |
|**totalBytesToDownload** | **Double** | Total bytes to download. |  [optional] |



## Enum: DownloadPhaseEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;Unknown&quot; |
| INITIALIZING | &quot;Initializing&quot; |
| DOWNLOADING | &quot;Downloading&quot; |
| VERIFYING | &quot;Verifying&quot; |



