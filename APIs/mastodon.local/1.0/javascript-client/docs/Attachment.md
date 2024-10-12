# MastodonApiSpecificationHttpsGithubComMastodonMastodon.Attachment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blurhash** | **String** | A hash computed by the [BlurHash algorithm](https://github.com/woltapp/blurhash), for generating colorful preview thumbnails when media has not been downloaded yet. | [optional] 
**description** | **String** | Alternate text that describes what is in the media attachment, to be used for the visually impaired or when media attachments do not load. | [optional] 
**id** | **String** | The ID of the attachment in the database. Cast from an integer but not guaranteed to be a number | 
**meta** | **Object** | Metadata returned by Paperclip. | [optional] 
**previewUrl** | **String** | The location of a scaled-down preview of the attachment. | 
**remoteUrl** | **String** | The location of the full-size original attachment on the remote website. String or null if the attachment is local. | [optional] 
**textUrl** | **String** | A shorter URL for the attachment. | [optional] 
**type** | **String** | The type of the attachment. | 
**url** | **String** | The location of the original full-size attachment. | 



## Enum: TypeEnum


* `unknown` (value: `"unknown"`)

* `image` (value: `"image"`)

* `gifv` (value: `"gifv"`)

* `video` (value: `"video"`)

* `audio` (value: `"audio"`)




