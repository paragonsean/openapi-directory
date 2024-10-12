# ExaVault.ResourceAttributes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessedAt** | **Date** | Date-time of the time when resource was accessed. | [optional] 
**accessedTime** | **Number** | UNIX timestamp of last access | [optional] 
**createdAt** | **Date** | Date-time of resource creation. | [optional] 
**createdBy** | **String** | Username of the creator. | [optional] 
**createdTime** | **Number** | UNIX timestamp of resource creation | [optional] 
**extension** | **String** | Resource extension. Property exists only if resource &#x60;type&#x60; is file. | [optional] 
**fileCount** | **Number** | Number of files within folder. null if resource type is a file. | [optional] 
**hash** | **String** | Unique hash of the resource. | [optional] 
**name** | **String** | Resource name, e.g. the name of the file or folder. | [optional] 
**path** | **String** | Full path to the resource. | [optional] 
**previewable** | **Boolean** | Can resource be previewed. Property equals &#x60;null&#x60; if resource &#x60;type&#x60; is dir. | [optional] 
**size** | **Number** | Resource size in bytes | [optional] 
**type** | **String** | Type of the resource. | [optional] 
**updatedAt** | **Date** | Date-time of resource modification. | [optional] 
**updatedTime** | **Number** | UNIX timestamp of resource modification | [optional] 
**uploadDate** | **Date** | Timestamp of resource upload. | [optional] 



## Enum: TypeEnum


* `file` (value: `"file"`)

* `dir` (value: `"dir"`)




