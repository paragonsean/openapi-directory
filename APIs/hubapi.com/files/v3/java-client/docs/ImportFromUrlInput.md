

# ImportFromUrlInput


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**access** | [**AccessEnum**](#AccessEnum) | PUBLIC_INDEXABLE: File is publicly accessible by anyone who has the URL. Search engines can index the file. PUBLIC_NOT_INDEXABLE: File is publicly accessible by anyone who has the URL. Search engines *can&#39;t* index the file. PRIVATE: File is NOT publicly accessible. Requires a signed URL to see content. Search engines *can&#39;t* index the file.  |  |
|**duplicateValidationScope** | [**DuplicateValidationScopeEnum**](#DuplicateValidationScopeEnum) | ENTIRE_PORTAL: Look for a duplicate file in the entire account. EXACT_FOLDER: Look for a duplicate file in the provided folder.  |  [optional] |
|**duplicateValidationStrategy** | [**DuplicateValidationStrategyEnum**](#DuplicateValidationStrategyEnum) | NONE: Do not run any duplicate validation. REJECT: Reject the upload if a duplicate is found. RETURN_EXISTING: If a duplicate file is found, do not upload a new file and return the found duplicate instead.  |  [optional] |
|**folderId** | **String** | One of folderId or folderPath is required. Destination folderId for the uploaded file. |  [optional] |
|**folderPath** | **String** | One of folderPath or folderId is required. Destination folder path for the uploaded file. If the folder path does not exist, there will be an attempt to create the folder path. |  [optional] |
|**name** | **String** | Name to give the resulting file in the file manager. |  [optional] |
|**overwrite** | **Boolean** | If true, will overwrite existing file if one with the same name and extension exists in the given folder. The overwritten file will be deleted and the uploaded file will take its place with a new ID. If unset or set as false, the new file&#39;s name will be updated to prevent colliding with existing file if one exists with the same path, name, and extension |  [optional] |
|**ttl** | **String** | Time to live. If specified the file will be deleted after the given time frame. If left unset, the file will exist indefinitely |  [optional] |
|**url** | **String** | URL to download the new file from. |  |



## Enum: AccessEnum

| Name | Value |
|---- | -----|
| PUBLIC_INDEXABLE | &quot;PUBLIC_INDEXABLE&quot; |
| PUBLIC_NOT_INDEXABLE | &quot;PUBLIC_NOT_INDEXABLE&quot; |
| HIDDEN_INDEXABLE | &quot;HIDDEN_INDEXABLE&quot; |
| HIDDEN_NOT_INDEXABLE | &quot;HIDDEN_NOT_INDEXABLE&quot; |
| HIDDEN_PRIVATE | &quot;HIDDEN_PRIVATE&quot; |
| PRIVATE | &quot;PRIVATE&quot; |



## Enum: DuplicateValidationScopeEnum

| Name | Value |
|---- | -----|
| ENTIRE_PORTAL | &quot;ENTIRE_PORTAL&quot; |
| EXACT_FOLDER | &quot;EXACT_FOLDER&quot; |



## Enum: DuplicateValidationStrategyEnum

| Name | Value |
|---- | -----|
| NONE | &quot;NONE&quot; |
| REJECT | &quot;REJECT&quot; |
| RETURN_EXISTING | &quot;RETURN_EXISTING&quot; |



