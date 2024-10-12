

# BackgroundJobLogEntry

Execution log of a background job.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**applyJobDetails** | [**ApplyJobDetails**](ApplyJobDetails.md) |  |  [optional] |
|**completionComment** | **String** | Output only. Job completion comment, such as how many entities were seeded, how many warnings were found during conversion, and similar information. |  [optional] [readonly] |
|**completionState** | [**CompletionStateEnum**](#CompletionStateEnum) | Output only. Job completion state, i.e. the final state after the job completed. |  [optional] [readonly] |
|**convertJobDetails** | [**ConvertJobDetails**](ConvertJobDetails.md) |  |  [optional] |
|**finishTime** | **String** | The timestamp when the background job was finished. |  [optional] |
|**id** | **String** | The background job log entry ID. |  [optional] |
|**importRulesJobDetails** | [**ImportRulesJobDetails**](ImportRulesJobDetails.md) |  |  [optional] |
|**jobType** | [**JobTypeEnum**](#JobTypeEnum) | The type of job that was executed. |  [optional] |
|**requestAutocommit** | **Boolean** | Output only. Whether the client requested the conversion workspace to be committed after a successful completion of the job. |  [optional] [readonly] |
|**seedJobDetails** | [**SeedJobDetails**](SeedJobDetails.md) |  |  [optional] |
|**startTime** | **String** | The timestamp when the background job was started. |  [optional] |



## Enum: CompletionStateEnum

| Name | Value |
|---- | -----|
| JOB_COMPLETION_STATE_UNSPECIFIED | &quot;JOB_COMPLETION_STATE_UNSPECIFIED&quot; |
| SUCCEEDED | &quot;SUCCEEDED&quot; |
| FAILED | &quot;FAILED&quot; |



## Enum: JobTypeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;BACKGROUND_JOB_TYPE_UNSPECIFIED&quot; |
| SOURCE_SEED | &quot;BACKGROUND_JOB_TYPE_SOURCE_SEED&quot; |
| CONVERT | &quot;BACKGROUND_JOB_TYPE_CONVERT&quot; |
| APPLY_DESTINATION | &quot;BACKGROUND_JOB_TYPE_APPLY_DESTINATION&quot; |
| IMPORT_RULES_FILE | &quot;BACKGROUND_JOB_TYPE_IMPORT_RULES_FILE&quot; |



