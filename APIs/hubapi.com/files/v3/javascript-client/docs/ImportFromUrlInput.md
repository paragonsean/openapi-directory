# FilesFiles.ImportFromUrlInput

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access** | **String** | PUBLIC_INDEXABLE: File is publicly accessible by anyone who has the URL. Search engines can index the file. PUBLIC_NOT_INDEXABLE: File is publicly accessible by anyone who has the URL. Search engines *can&#39;t* index the file. PRIVATE: File is NOT publicly accessible. Requires a signed URL to see content. Search engines *can&#39;t* index the file.  | 
**duplicateValidationScope** | **String** | ENTIRE_PORTAL: Look for a duplicate file in the entire account. EXACT_FOLDER: Look for a duplicate file in the provided folder.  | [optional] 
**duplicateValidationStrategy** | **String** | NONE: Do not run any duplicate validation. REJECT: Reject the upload if a duplicate is found. RETURN_EXISTING: If a duplicate file is found, do not upload a new file and return the found duplicate instead.  | [optional] 
**folderId** | **String** | One of folderId or folderPath is required. Destination folderId for the uploaded file. | [optional] 
**folderPath** | **String** | One of folderPath or folderId is required. Destination folder path for the uploaded file. If the folder path does not exist, there will be an attempt to create the folder path. | [optional] 
**name** | **String** | Name to give the resulting file in the file manager. | [optional] 
**overwrite** | **Boolean** | If true, will overwrite existing file if one with the same name and extension exists in the given folder. The overwritten file will be deleted and the uploaded file will take its place with a new ID. If unset or set as false, the new file&#39;s name will be updated to prevent colliding with existing file if one exists with the same path, name, and extension | [optional] 
**ttl** | **String** | Time to live. If specified the file will be deleted after the given time frame. If left unset, the file will exist indefinitely | [optional] 
**url** | **String** | URL to download the new file from. | 



## Enum: AccessEnum


* `PUBLIC_INDEXABLE` (value: `"PUBLIC_INDEXABLE"`)

* `PUBLIC_NOT_INDEXABLE` (value: `"PUBLIC_NOT_INDEXABLE"`)

* `HIDDEN_INDEXABLE` (value: `"HIDDEN_INDEXABLE"`)

* `HIDDEN_NOT_INDEXABLE` (value: `"HIDDEN_NOT_INDEXABLE"`)

* `HIDDEN_PRIVATE` (value: `"HIDDEN_PRIVATE"`)

* `PRIVATE` (value: `"PRIVATE"`)





## Enum: DuplicateValidationScopeEnum


* `ENTIRE_PORTAL` (value: `"ENTIRE_PORTAL"`)

* `EXACT_FOLDER` (value: `"EXACT_FOLDER"`)





## Enum: DuplicateValidationStrategyEnum


* `NONE` (value: `"NONE"`)

* `REJECT` (value: `"REJECT"`)

* `RETURN_EXISTING` (value: `"RETURN_EXISTING"`)




