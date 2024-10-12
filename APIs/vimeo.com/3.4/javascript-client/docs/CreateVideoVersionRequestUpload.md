# Vimeo.CreateVideoVersionRequestUpload

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**approach** | **String** | Upload approach | 
**link** | **String** | If your upload approach is pull, Vimeo will download the video hosted at this public URL. This URL must be valid for at least 24 hours. | [optional] 
**redirectUrl** | **String** | The app&#39;s redirect URL. Use this parameter when &#x60;approach&#x60; is &#x60;post&#x60;. | [optional] 
**size** | **String** | Upload size | [optional] 



## Enum: ApproachEnum


* `post` (value: `"post"`)

* `pull` (value: `"pull"`)

* `streaming` (value: `"streaming"`)

* `tus` (value: `"tus"`)




