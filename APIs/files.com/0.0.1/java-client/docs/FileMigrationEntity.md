

# FileMigrationEntity

Show File Migration

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**destPath** | **String** | Destination path |  [optional] |
|**filesMoved** | **Integer** | Number of files processed |  [optional] |
|**filesTotal** | **Integer** | Deprecated: used to return a count of the applicable files.  Currently returns 0 always.  On remote servers, it is not possible to reliably determine the number of affected files for every migration operation. |  [optional] |
|**id** | **Integer** | File migration ID |  [optional] |
|**logUrl** | **String** | Link to download the log file for this migration. |  [optional] |
|**operation** | [**OperationEnum**](#OperationEnum) | The type of operation |  [optional] |
|**path** | **String** | Source path |  [optional] |
|**region** | **String** | Region |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Status |  [optional] |



## Enum: OperationEnum

| Name | Value |
|---- | -----|
| DELETE | &quot;delete&quot; |
| MOVE | &quot;move&quot; |
| COPY | &quot;copy&quot; |
| REGIONAL_MIGRATION | &quot;regional_migration&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| PENDING | &quot;pending&quot; |
| COUNTING | &quot;counting&quot; |
| PROCESSING | &quot;processing&quot; |
| COMPLETED | &quot;completed&quot; |
| PROCESSING_SUBFOLDERS | &quot;processing_subfolders&quot; |
| FINISHING | &quot;finishing&quot; |
| CREATING_DEST_FOLDER | &quot;creating_dest_folder&quot; |
| WAITING_FOR_OTHER_JOBS | &quot;waiting_for_other_jobs&quot; |
| WAITING_FOR_ALL_FILES | &quot;waiting_for_all_files&quot; |
| WAITING_FOR_PENDING_SUBFOLDERS | &quot;waiting_for_pending_subfolders&quot; |
| WAITING_FOR_ALL_SUBFOLDERS | &quot;waiting_for_all_subfolders&quot; |
| FAILED | &quot;failed&quot; |
| WAITING_FOR_ENQUEUED_OPERATIONS | &quot;waiting_for_enqueued_operations&quot; |
| UNUSED | &quot;unused&quot; |
| PROCESSING_RECURSIVELY | &quot;processing_recursively&quot; |
| REMOVING_DEFERRED_FOLDERS | &quot;removing_deferred_folders&quot; |



