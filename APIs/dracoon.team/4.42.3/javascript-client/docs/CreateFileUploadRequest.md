# DracoonApi.CreateFileUploadRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**classification** | **Number** | Classification ID:  * &#x60;1&#x60; - public  * &#x60;2&#x60; - internal  * &#x60;3&#x60; - confidential  * &#x60;4&#x60; - strictly confidential    (default: classification from parent room) | [optional] 
**directS3Upload** | **Boolean** | &amp;#128640; Since v4.15.0  Upload direct to S3 | [optional] [default to false]
**expiration** | [**ObjectExpiration**](ObjectExpiration.md) |  | [optional] 
**name** | **String** | File name | 
**notes** | **String** | User notes  Use empty string to remove. | [optional] 
**parentId** | **Number** | Parent node ID (room or folder) | 
**size** | **Number** | File size in byte | [optional] 
**timestampCreation** | **Date** | &amp;#128640; Since v4.22.0  Time the node was created on external file system  (default: current server datetime in UTC format) | [optional] 
**timestampModification** | **Date** | &amp;#128640; Since v4.22.0  Time the content of a node was last modified on external file system  (default: current server datetime in UTC format) | [optional] 



## Enum: ClassificationEnum


* `1` (value: `1`)

* `2` (value: `2`)

* `3` (value: `3`)

* `4` (value: `4`)




