# DracoonApi.DeletedNode

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessedAt** | **Date** | Last access date | [optional] 
**classification** | **Number** | Classification ID:  * &#x60;1&#x60; - public  * &#x60;2&#x60; - internal  * &#x60;3&#x60; - confidential  * &#x60;4&#x60; - strictly confidential    (default: classification from parent room) | [optional] 
**createdAt** | **Date** | Creation date | [optional] 
**createdBy** | [**UserInfo**](UserInfo.md) |  | [optional] 
**deletedAt** | **Date** | Deletion date | [optional] 
**deletedBy** | [**UserInfo**](UserInfo.md) |  | [optional] 
**expireAt** | **Date** | Expiration date | [optional] 
**id** | **Number** | Node ID | [optional] 
**isEncrypted** | **Boolean** | Encryption state | [optional] 
**name** | **String** | Node name | 
**notes** | **String** | User notes | [optional] 
**parentId** | **Number** | Parent node ID (room or folder) | 
**parentPath** | **String** | Parent node path  &#x60;/&#x60; if node is a root node (room) | 
**referenceId** | **Number** | &amp;#128640; Since v4.37.0  Reference ID. Identical across all versions of a file | [optional] 
**size** | **Number** | Node size in byte | [optional] 
**type** | **String** | Node type | 
**updatedAt** | **Date** | Modification date | [optional] 
**updatedBy** | [**UserInfo**](UserInfo.md) |  | [optional] 



## Enum: ClassificationEnum


* `1` (value: `1`)

* `2` (value: `2`)

* `3` (value: `3`)

* `4` (value: `4`)





## Enum: TypeEnum


* `folder` (value: `"folder"`)

* `file` (value: `"file"`)




