

# ReleasesUpdateReleaseUploadStatus200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **UUID** | The ID for the upload. |  |
|**uploadStatus** | [**UploadStatusEnum**](#UploadStatusEnum) | The current upload status. |  |



## Enum: UploadStatusEnum

| Name | Value |
|---- | -----|
| UPLOAD_STARTED | &quot;uploadStarted&quot; |
| UPLOAD_FINISHED | &quot;uploadFinished&quot; |
| UPLOAD_CANCELED | &quot;uploadCanceled&quot; |
| READY_TO_BE_PUBLISHED | &quot;readyToBePublished&quot; |
| MALWARE_DETECTED | &quot;malwareDetected&quot; |
| ERROR | &quot;error&quot; |



