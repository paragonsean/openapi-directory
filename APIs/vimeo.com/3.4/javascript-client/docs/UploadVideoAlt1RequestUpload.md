# Vimeo.UploadVideoAlt1RequestUpload

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**approach** | **String** | The upload approach. | 
**link** | **String** | The public URL at which the video is hosted. The URL must be valid for at least 24 hours. Use this parameter when &#x60;approach&#x60; is &#x60;pull&#x60;. | [optional] 
**redirectUrl** | **String** | The app&#39;s redirect URL. Use this parameter when &#x60;approach&#x60; is &#x60;post&#x60;. | [optional] 
**size** | **String** | The size in bytes of the video to upload. | [optional] 



## Enum: ApproachEnum


* `post` (value: `"post"`)

* `pull` (value: `"pull"`)

* `streaming` (value: `"streaming"`)

* `tus` (value: `"tus"`)




