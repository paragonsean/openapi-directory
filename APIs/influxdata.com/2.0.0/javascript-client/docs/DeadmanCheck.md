# InfluxOssApiService.DeadmanCheck

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createdAt** | **Date** |  | [optional] [readonly] 
**description** | **String** | An optional description of the check. | [optional] 
**id** | **String** |  | [optional] [readonly] 
**labels** | [**[Label]**](Label.md) |  | [optional] 
**lastRunError** | **String** |  | [optional] [readonly] 
**lastRunStatus** | **String** |  | [optional] [readonly] 
**latestCompleted** | **Date** | Timestamp of latest scheduled, completed run, RFC3339. | [optional] [readonly] 
**links** | [**CheckBaseLinks**](CheckBaseLinks.md) |  | [optional] 
**name** | **String** |  | 
**orgID** | **String** | The ID of the organization that owns this check. | 
**ownerID** | **String** | The ID of creator used to create this check. | [optional] [readonly] 
**query** | [**DashboardQuery**](DashboardQuery.md) |  | 
**status** | [**TaskStatusType**](TaskStatusType.md) |  | [optional] 
**taskID** | **String** | The ID of the task associated with this check. | [optional] 
**updatedAt** | **Date** |  | [optional] [readonly] 
**every** | **String** | Check repetition interval. | [optional] 
**level** | [**CheckStatusLevel**](CheckStatusLevel.md) |  | [optional] 
**offset** | **String** | Duration to delay after the schedule, before executing check. | [optional] 
**reportZero** | **Boolean** | If only zero values reported since time, trigger an alert | [optional] 
**staleTime** | **String** | String duration for time that a series is considered stale and should not trigger deadman. | [optional] 
**statusMessageTemplate** | **String** | The template used to generate and write a status message. | [optional] 
**tags** | [**[DeadmanCheckAllOfTags]**](DeadmanCheckAllOfTags.md) | List of tags to write to each status. | [optional] 
**timeSince** | **String** | String duration before deadman triggers. | [optional] 
**type** | **String** |  | 



## Enum: LastRunStatusEnum


* `failed` (value: `"failed"`)

* `success` (value: `"success"`)

* `canceled` (value: `"canceled"`)





## Enum: TypeEnum


* `deadman` (value: `"deadman"`)




