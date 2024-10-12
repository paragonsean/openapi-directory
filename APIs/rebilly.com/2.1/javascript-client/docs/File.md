# RebillyRestApi.File

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**[FileLinksInner]**](FileLinksInner.md) | The links related to resource. | [optional] [readonly] 
**createdTime** | **Date** | The upload date/time. | [optional] [readonly] 
**description** | **String** | The File description. | [optional] 
**extension** | **String** | The File extension. | [optional] 
**height** | **Number** | Image height, applicable to images only. | [optional] [readonly] 
**id** | **String** | The resource ID. Defaults to UUID v4. | [optional] [readonly] 
**isPublic** | **Boolean** | Is the file available publicly (without authentication). If true, the permalink in the _links section contains the public URL. | [optional] 
**mime** | **String** | The mime type. | [optional] [readonly] 
**name** | **String** | Original File name. | [optional] 
**sha1** | **String** | Hash sum of the file. | [optional] [readonly] 
**size** | **Number** | The File size in bytes. | [optional] [readonly] 
**tags** | **[String]** | The tags list. | [optional] 
**updatedTime** | **Date** | The latest update date/time. | [optional] [readonly] 
**width** | **Number** | Image width, applicable to images only. | [optional] [readonly] 



## Enum: MimeEnum


* `image/png` (value: `"image/png"`)

* `image/jpeg` (value: `"image/jpeg"`)

* `image/gif` (value: `"image/gif"`)

* `application/pdf` (value: `"application/pdf"`)

* `audio/mpeg` (value: `"audio/mpeg"`)




