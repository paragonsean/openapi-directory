# AppCenterClient.GetReleaseStatusResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errorDetails** | **String** | Details describing what went wrong processing the upload. Will only be set if status &#x3D; &#39;error&#39;. | [optional] 
**id** | **String** | The ID for the upload. | 
**releaseDistinctId** | **Number** | The distinct ID of the release. Will only be set when the status &#x3D; &#39;readyToBePublished&#39;. | [optional] 
**releaseUrl** | **Object** | The URL of the release. Will only be set when the status &#x3D; &#39;readyToBePublished&#39;. | [optional] 
**uploadStatus** | **String** | The current upload status. | 



## Enum: UploadStatusEnum


* `uploadStarted` (value: `"uploadStarted"`)

* `uploadFinished` (value: `"uploadFinished"`)

* `readyToBePublished` (value: `"readyToBePublished"`)

* `malwareDetected` (value: `"malwareDetected"`)

* `error` (value: `"error"`)




