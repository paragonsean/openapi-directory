# DatabaseMigrationApi.BackgroundJobLogEntry

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applyJobDetails** | [**ApplyJobDetails**](ApplyJobDetails.md) |  | [optional] 
**completionComment** | **String** | Output only. Job completion comment, such as how many entities were seeded, how many warnings were found during conversion, and similar information. | [optional] [readonly] 
**completionState** | **String** | Output only. Job completion state, i.e. the final state after the job completed. | [optional] [readonly] 
**convertJobDetails** | [**ConvertJobDetails**](ConvertJobDetails.md) |  | [optional] 
**finishTime** | **String** | The timestamp when the background job was finished. | [optional] 
**id** | **String** | The background job log entry ID. | [optional] 
**importRulesJobDetails** | [**ImportRulesJobDetails**](ImportRulesJobDetails.md) |  | [optional] 
**jobType** | **String** | The type of job that was executed. | [optional] 
**requestAutocommit** | **Boolean** | Output only. Whether the client requested the conversion workspace to be committed after a successful completion of the job. | [optional] [readonly] 
**seedJobDetails** | [**SeedJobDetails**](SeedJobDetails.md) |  | [optional] 
**startTime** | **String** | The timestamp when the background job was started. | [optional] 



## Enum: CompletionStateEnum


* `JOB_COMPLETION_STATE_UNSPECIFIED` (value: `"JOB_COMPLETION_STATE_UNSPECIFIED"`)

* `SUCCEEDED` (value: `"SUCCEEDED"`)

* `FAILED` (value: `"FAILED"`)





## Enum: JobTypeEnum


* `UNSPECIFIED` (value: `"BACKGROUND_JOB_TYPE_UNSPECIFIED"`)

* `SOURCE_SEED` (value: `"BACKGROUND_JOB_TYPE_SOURCE_SEED"`)

* `CONVERT` (value: `"BACKGROUND_JOB_TYPE_CONVERT"`)

* `APPLY_DESTINATION` (value: `"BACKGROUND_JOB_TYPE_APPLY_DESTINATION"`)

* `IMPORT_RULES_FILE` (value: `"BACKGROUND_JOB_TYPE_IMPORT_RULES_FILE"`)




