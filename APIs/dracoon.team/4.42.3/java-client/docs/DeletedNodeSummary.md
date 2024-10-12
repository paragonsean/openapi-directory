

# DeletedNodeSummary

Deleted node information (Deleted node can be a folder or file)

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cntVersions** | **Integer** | Number of deleted versions of this file |  |
|**firstDeletedAt** | **OffsetDateTime** | First deleted version |  |
|**lastDeletedAt** | **OffsetDateTime** | Last deleted version |  |
|**lastDeletedNodeId** | **Long** | Node ID of last deleted version |  |
|**name** | **String** | Node name |  |
|**parentId** | **Long** | Parent node ID (room or folder) |  |
|**parentPath** | **String** | Parent node path  &#x60;/&#x60; if node is a root node (room) |  |
|**referenceId** | **Long** | &amp;#128640; Since v4.37.0  Reference ID. Identical across all versions of a file |  [optional] |
|**timestampCreation** | **OffsetDateTime** | &amp;#128640; Since v4.22.0  Time the node was created on external file system |  [optional] |
|**timestampModification** | **OffsetDateTime** | &amp;#128640; Since v4.22.0  Time the content of a node was last modified on external file system |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Node type |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| FOLDER | &quot;folder&quot; |
| FILE | &quot;file&quot; |



