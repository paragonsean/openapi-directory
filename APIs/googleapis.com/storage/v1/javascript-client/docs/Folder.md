# CloudStorageJsonApi.Folder

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket** | **String** | The name of the bucket containing this folder. | [optional] 
**createTime** | **Date** | The creation time of the folder in RFC 3339 format. | [optional] 
**id** | **String** | The ID of the folder, including the bucket name, folder name. | [optional] 
**kind** | **String** | The kind of item this is. For folders, this is always storage#folder. | [optional] [default to &#39;storage#folder&#39;]
**metageneration** | **String** | The version of the metadata for this folder. Used for preconditions and for detecting changes in metadata. | [optional] 
**name** | **String** | The name of the folder. Required if not specified by URL parameter. | [optional] 
**pendingRenameInfo** | [**FolderPendingRenameInfo**](FolderPendingRenameInfo.md) |  | [optional] 
**selfLink** | **String** | The link to this folder. | [optional] 
**updateTime** | **Date** | The modification time of the folder metadata in RFC 3339 format. | [optional] 


