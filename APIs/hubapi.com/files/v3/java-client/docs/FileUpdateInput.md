

# FileUpdateInput

Object for updating files.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**access** | [**AccessEnum**](#AccessEnum) | NONE: Do not run any duplicate validation. REJECT: Reject the upload if a duplicate is found. RETURN_EXISTING: If a duplicate file is found, do not upload a new file and return the found duplicate instead.  |  [optional] |
|**expiresAt** | **Long** |  |  [optional] |
|**isUsableInContent** | **Boolean** | Mark whether the file should be used in new content or not. |  [optional] |
|**name** | **String** | New name for the file. |  [optional] |
|**parentFolderId** | **String** | FolderId where the file should be moved to. folderId and folderPath parameters cannot be set at the same time. |  [optional] |
|**parentFolderPath** | **String** | Folder path where the file should be moved to. folderId and folderPath parameters cannot be set at the same time. |  [optional] |



## Enum: AccessEnum

| Name | Value |
|---- | -----|
| PUBLIC_INDEXABLE | &quot;PUBLIC_INDEXABLE&quot; |
| PUBLIC_NOT_INDEXABLE | &quot;PUBLIC_NOT_INDEXABLE&quot; |
| HIDDEN_INDEXABLE | &quot;HIDDEN_INDEXABLE&quot; |
| HIDDEN_NOT_INDEXABLE | &quot;HIDDEN_NOT_INDEXABLE&quot; |
| HIDDEN_PRIVATE | &quot;HIDDEN_PRIVATE&quot; |
| PRIVATE | &quot;PRIVATE&quot; |



