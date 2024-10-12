# DracoonApi.CreateFolderRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**classification** | **Number** | &amp;#128640; Since v4.30.0  Classification ID:  * &#x60;1&#x60; - public  * &#x60;2&#x60; - internal  * &#x60;3&#x60; - confidential  * &#x60;4&#x60; - strictly confidential    Provided (or default) classification is taken from room  when file gets uploaded without any classification. | [optional] 
**name** | **String** | Name | 
**notes** | **String** | User notes  Use empty string to remove. | [optional] 
**parentId** | **Number** | Parent node ID (room or folder) | 
**timestampCreation** | **Date** | &amp;#128640; Since v4.22.0  Time the node was created on external file system  (default: current server datetime in UTC format) | [optional] 
**timestampModification** | **Date** | &amp;#128640; Since v4.22.0  Time the content of a node was last modified on external file system  (default: current server datetime in UTC format) | [optional] 



## Enum: ClassificationEnum


* `1` (value: `1`)

* `2` (value: `2`)

* `3` (value: `3`)

* `4` (value: `4`)




