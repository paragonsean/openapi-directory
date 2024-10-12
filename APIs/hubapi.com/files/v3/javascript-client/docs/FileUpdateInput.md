# FilesFiles.FileUpdateInput

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access** | **String** | NONE: Do not run any duplicate validation. REJECT: Reject the upload if a duplicate is found. RETURN_EXISTING: If a duplicate file is found, do not upload a new file and return the found duplicate instead.  | [optional] 
**expiresAt** | **Number** |  | [optional] 
**isUsableInContent** | **Boolean** | Mark whether the file should be used in new content or not. | [optional] 
**name** | **String** | New name for the file. | [optional] 
**parentFolderId** | **String** | FolderId where the file should be moved to. folderId and folderPath parameters cannot be set at the same time. | [optional] 
**parentFolderPath** | **String** | Folder path where the file should be moved to. folderId and folderPath parameters cannot be set at the same time. | [optional] 



## Enum: AccessEnum


* `PUBLIC_INDEXABLE` (value: `"PUBLIC_INDEXABLE"`)

* `PUBLIC_NOT_INDEXABLE` (value: `"PUBLIC_NOT_INDEXABLE"`)

* `HIDDEN_INDEXABLE` (value: `"HIDDEN_INDEXABLE"`)

* `HIDDEN_NOT_INDEXABLE` (value: `"HIDDEN_NOT_INDEXABLE"`)

* `HIDDEN_PRIVATE` (value: `"HIDDEN_PRIVATE"`)

* `PRIVATE` (value: `"PRIVATE"`)




