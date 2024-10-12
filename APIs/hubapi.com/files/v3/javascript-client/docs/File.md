# FilesFiles.File

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access** | **String** | File access. Can be PUBLIC_INDEXABLE, PUBLIC_NOT_INDEXABLE, PRIVATE. | 
**archived** | **Boolean** | If the file is deleted. | 
**archivedAt** | **Date** | Deletion time of the file object. | [optional] 
**createdAt** | **Date** | Creation time of the file object. | 
**defaultHostingUrl** | **String** | Default hosting URL of the file. This will use one of HubSpot&#39;s provided URLs to serve the file. | [optional] 
**encoding** | **String** | Encoding of the file. | [optional] 
**expiresAt** | **Number** |  | [optional] 
**extension** | **String** | Extension of the file. ex: .jpg, .png, .gif, .pdf, etc. | [optional] 
**height** | **Number** | For image and video files, the height of the content. | [optional] 
**id** | **String** | File ID. | 
**isUsableInContent** | **Boolean** | Previously \&quot;archied\&quot;. Indicates if the file should be used when creating new content like web pages. | [optional] 
**name** | **String** | Name of the file. | [optional] 
**parentFolderId** | **String** | ID of the folder the file is in. | [optional] 
**path** | **String** | Path of the file in the file manager. | [optional] 
**size** | **Number** | Size of the file in bytes. | [optional] 
**type** | **String** | Type of the file. Can be IMG, DOCUMENT, AUDIO, MOVIE, or OTHER. | [optional] 
**updatedAt** | **Date** | Timestamp of the latest update to the file. | 
**url** | **String** | URL of the given file. This URL can change depending on the domain settings of the account. Will use the select file hosting domain. | [optional] 
**width** | **Number** | For image and video files, the width of the content. | [optional] 



## Enum: AccessEnum


* `PUBLIC_INDEXABLE` (value: `"PUBLIC_INDEXABLE"`)

* `PUBLIC_NOT_INDEXABLE` (value: `"PUBLIC_NOT_INDEXABLE"`)

* `HIDDEN_INDEXABLE` (value: `"HIDDEN_INDEXABLE"`)

* `HIDDEN_NOT_INDEXABLE` (value: `"HIDDEN_NOT_INDEXABLE"`)

* `HIDDEN_PRIVATE` (value: `"HIDDEN_PRIVATE"`)

* `PRIVATE` (value: `"PRIVATE"`)




