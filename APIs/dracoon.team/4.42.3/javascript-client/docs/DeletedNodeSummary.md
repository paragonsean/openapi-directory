# DracoonApi.DeletedNodeSummary

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cntVersions** | **Number** | Number of deleted versions of this file | 
**firstDeletedAt** | **Date** | First deleted version | 
**lastDeletedAt** | **Date** | Last deleted version | 
**lastDeletedNodeId** | **Number** | Node ID of last deleted version | 
**name** | **String** | Node name | 
**parentId** | **Number** | Parent node ID (room or folder) | 
**parentPath** | **String** | Parent node path  &#x60;/&#x60; if node is a root node (room) | 
**referenceId** | **Number** | &amp;#128640; Since v4.37.0  Reference ID. Identical across all versions of a file | [optional] 
**timestampCreation** | **Date** | &amp;#128640; Since v4.22.0  Time the node was created on external file system | [optional] 
**timestampModification** | **Date** | &amp;#128640; Since v4.22.0  Time the content of a node was last modified on external file system | [optional] 
**type** | **String** | Node type | 



## Enum: TypeEnum


* `folder` (value: `"folder"`)

* `file` (value: `"file"`)




