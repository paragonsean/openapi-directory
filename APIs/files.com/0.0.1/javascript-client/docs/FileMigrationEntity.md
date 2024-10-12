# FilesComApi.FileMigrationEntity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destPath** | **String** | Destination path | [optional] 
**filesMoved** | **Number** | Number of files processed | [optional] 
**filesTotal** | **Number** | Deprecated: used to return a count of the applicable files.  Currently returns 0 always.  On remote servers, it is not possible to reliably determine the number of affected files for every migration operation. | [optional] 
**id** | **Number** | File migration ID | [optional] 
**logUrl** | **String** | Link to download the log file for this migration. | [optional] 
**operation** | **String** | The type of operation | [optional] 
**path** | **String** | Source path | [optional] 
**region** | **String** | Region | [optional] 
**status** | **String** | Status | [optional] 



## Enum: OperationEnum


* `delete` (value: `"delete"`)

* `move` (value: `"move"`)

* `copy` (value: `"copy"`)

* `regional_migration` (value: `"regional_migration"`)





## Enum: StatusEnum


* `pending` (value: `"pending"`)

* `counting` (value: `"counting"`)

* `processing` (value: `"processing"`)

* `completed` (value: `"completed"`)

* `processing_subfolders` (value: `"processing_subfolders"`)

* `finishing` (value: `"finishing"`)

* `creating_dest_folder` (value: `"creating_dest_folder"`)

* `waiting_for_other_jobs` (value: `"waiting_for_other_jobs"`)

* `waiting_for_all_files` (value: `"waiting_for_all_files"`)

* `waiting_for_pending_subfolders` (value: `"waiting_for_pending_subfolders"`)

* `waiting_for_all_subfolders` (value: `"waiting_for_all_subfolders"`)

* `failed` (value: `"failed"`)

* `waiting_for_enqueued_operations` (value: `"waiting_for_enqueued_operations"`)

* `unused` (value: `"unused"`)

* `processing_recursively` (value: `"processing_recursively"`)

* `removing_deferred_folders` (value: `"removing_deferred_folders"`)




