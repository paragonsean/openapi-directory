

# UnifiedFile


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdAt** | **OffsetDateTime** | The date and time when the object was created. |  [optional] [readonly] |
|**createdBy** | **String** | The user who created the object. |  [optional] [readonly] |
|**customMappings** | **Object** | When custom mappings are configured on the resource, the result is included here. |  [optional] |
|**description** | **String** | Optional description of the file |  [optional] |
|**downloadable** | **Boolean** | Whether the current user can download this file |  [optional] |
|**downstreamId** | **String** | The third-party API ID of original entity |  [optional] [readonly] |
|**exportFormats** | **List&lt;String&gt;** | The available file formats when exporting this file. |  [optional] |
|**exportable** | **Boolean** | Whether the current file is exportable to other file formats. This property is relevant for proprietary file formats such as Google Docs or Dropbox Paper. |  [optional] |
|**id** | **String** | A unique identifier for an object. |  [readonly] |
|**mimeType** | **String** | The MIME type of the file. |  [optional] |
|**name** | **String** | The name of the file |  |
|**owner** | [**Owner**](Owner.md) |  |  [optional] |
|**parentFolders** | [**List&lt;LinkedFolder&gt;**](LinkedFolder.md) | The parent folders of the file, starting from the root |  [optional] |
|**parentFoldersComplete** | **Boolean** | Whether the list of parent folders is complete. Some connectors only return the direct parent of a file |  [optional] |
|**path** | **String** | The full path of the file or folder (includes the file name) |  [optional] |
|**permissions** | [**UnifiedFilePermissions**](UnifiedFilePermissions.md) |  |  [optional] |
|**size** | **Integer** | The size of the file in bytes |  [optional] |
|**type** | **FileType** |  |  |
|**updatedAt** | **OffsetDateTime** | The date and time when the object was last updated. |  [optional] [readonly] |
|**updatedBy** | **String** | The user who last updated the object. |  [optional] [readonly] |



