# MastodonApiSpecificationHttpsGithubComMastodonMastodon.Card

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorName** | **String** | The author of the original resource. | [optional] 
**authorUrl** | **String** | A link to the author of the original resource. | [optional] 
**blurhash** | **String** | A hash computed by the [BlurHash algorithm](https://github.com/woltapp/blurhash), for generating colorful preview thumbnails when media has not been downloaded yet. | [optional] 
**description** | **String** | Description of preview. | 
**height** | **Number** | Height of preview, in pixels. | [optional] 
**html** | **String** | HTML to be used for generating the preview card. | [optional] 
**image** | **String** | Preview thumbnail (URL). | [optional] 
**providerName** | **String** | The provider of the original resource. | [optional] 
**providerUrl** | **String** | A link to the provider of the original resource. | [optional] 
**title** | **String** | Title of linked resource. | 
**type** | **String** | The type of the preview card. String (Enumerable, oneOf). | 
**url** | **String** | Location of linked resource. | 
**width** | **Number** | Width of preview, in pixels. | [optional] 



## Enum: TypeEnum


* `link` (value: `"link"`)

* `photo` (value: `"photo"`)

* `video` (value: `"video"`)

* `rich` (value: `"rich"`)




