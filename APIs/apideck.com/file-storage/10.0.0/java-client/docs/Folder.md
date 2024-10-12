

# Folder


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdAt** | **OffsetDateTime** | The date and time when the object was created. |  [optional] [readonly] |
|**createdBy** | **String** | The user who created the object. |  [optional] [readonly] |
|**customMappings** | **Object** | When custom mappings are configured on the resource, the result is included here. |  [optional] |
|**description** | **String** | Optional description of the folder |  [optional] |
|**id** | **String** | A unique identifier for an object. |  [optional] [readonly] |
|**name** | **String** | The name of the folder |  |
|**owner** | [**Owner**](Owner.md) |  |  [optional] |
|**parentFolders** | [**List&lt;LinkedFolder&gt;**](LinkedFolder.md) | The parent folders of the file, starting from the root |  |
|**parentFoldersComplete** | **Boolean** | Whether the list of parent folder is complete. Some connectors only return the direct parent of a folder |  [optional] [readonly] |
|**path** | **String** | The full path of the folder (includes the folder name) |  [optional] [readonly] |
|**size** | **Integer** | The size of the folder in bytes |  [optional] [readonly] |
|**updatedAt** | **OffsetDateTime** | The date and time when the object was last updated. |  [optional] [readonly] |
|**updatedBy** | **String** | The user who last updated the object. |  [optional] [readonly] |



