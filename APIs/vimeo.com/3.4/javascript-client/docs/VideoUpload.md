# Vimeo.VideoUpload

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**approach** | **String** | The approach for uploading the video. | [optional] 
**completeUri** | **String** | The URI for completing the upload. | [optional] 
**form** | **String** | The HTML form for uploading a video through the post approach. | [optional] 
**link** | **String** | The link of the video to capture through the pull approach. | [optional] 
**redirectUrl** | **String** | The redirect URL for the upload app. | [optional] 
**size** | **Number** | The file size in bytes of the uploaded video. | [optional] 
**status** | **String** | The status code for the availability of the uploaded video:  Option descriptions:  * &#x60;complete&#x60; - The upload is complete.  * &#x60;error&#x60; - The upload ended with an error.  * &#x60;in_progress&#x60; - The upload is underway.  | 
**uploadLink** | **String** | The link for sending video file data. | [optional] 



## Enum: ApproachEnum


* `post` (value: `"post"`)

* `pull` (value: `"pull"`)

* `streaming` (value: `"streaming"`)

* `tus` (value: `"tus"`)





## Enum: StatusEnum


* `complete` (value: `"complete"`)

* `error` (value: `"error"`)

* `in_progress` (value: `"in_progress"`)




