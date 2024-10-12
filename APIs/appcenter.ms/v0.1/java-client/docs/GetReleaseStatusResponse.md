

# GetReleaseStatusResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**errorDetails** | **String** | Details describing what went wrong processing the upload. Will only be set if status &#x3D; &#39;error&#39;. |  [optional] |
|**id** | **UUID** | The ID for the upload. |  |
|**releaseDistinctId** | **BigDecimal** | The distinct ID of the release. Will only be set when the status &#x3D; &#39;readyToBePublished&#39;. |  [optional] |
|**releaseUrl** | **Object** | The URL of the release. Will only be set when the status &#x3D; &#39;readyToBePublished&#39;. |  [optional] |
|**uploadStatus** | [**UploadStatusEnum**](#UploadStatusEnum) | The current upload status. |  |



## Enum: UploadStatusEnum

| Name | Value |
|---- | -----|
| UPLOAD_STARTED | &quot;uploadStarted&quot; |
| UPLOAD_FINISHED | &quot;uploadFinished&quot; |
| READY_TO_BE_PUBLISHED | &quot;readyToBePublished&quot; |
| MALWARE_DETECTED | &quot;malwareDetected&quot; |
| ERROR | &quot;error&quot; |



