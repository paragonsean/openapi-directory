# DataBoxEdgeManagementClient.UpdateDownloadProgress

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**downloadPhase** | **String** | The download phase. | [optional] [readonly] 
**numberOfUpdatesDownloaded** | **Number** | Number of updates downloaded. | [optional] [readonly] 
**numberOfUpdatesToDownload** | **Number** | Number of updates to download. | [optional] [readonly] 
**percentComplete** | **Number** | Percentage of completion. | [optional] [readonly] 
**totalBytesDownloaded** | **Number** | Total bytes downloaded. | [optional] [readonly] 
**totalBytesToDownload** | **Number** | Total bytes to download. | [optional] [readonly] 



## Enum: DownloadPhaseEnum


* `Unknown` (value: `"Unknown"`)

* `Initializing` (value: `"Initializing"`)

* `Downloading` (value: `"Downloading"`)

* `Verifying` (value: `"Verifying"`)




