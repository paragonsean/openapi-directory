

# FolderUpdateInput

Object for updating folders.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | ID of the folder to change. |  |
|**name** | **String** | New name. If specified the folder&#39;s name and fullPath will change. All children of the folder will be updated accordingly. |  [optional] |
|**parentFolderId** | **Long** | New parent folderId. If changed, the folder and all it&#39;s children will be moved into the specified folder. parentFolderId and parentFolderPath cannot be specified at the same time. |  [optional] |



