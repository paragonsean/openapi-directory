# Vimeo.EditTextTrackRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **Boolean** | Whether the text track is active, meaning that it appears in the player. Only one text track per language, and type, can be active. | [optional] 
**language** | **String** | The language of the text track. For a full list of valid languages, use the [/languages?filter&#x3D;texttracks](https://developer.vimeo.com/api/endpoints/videos#GET/languages) endpoint. | [optional] 
**name** | **String** | The name of the text track. | [optional] 
**type** | **String** | The text track type. | [optional] 



## Enum: TypeEnum


* `captions` (value: `"captions"`)

* `chapters` (value: `"chapters"`)

* `descriptions` (value: `"descriptions"`)

* `metadata` (value: `"metadata"`)

* `subtitles` (value: `"subtitles"`)




