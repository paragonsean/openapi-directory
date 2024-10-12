# SchedulerManagementClient.JobHistoryDefinitionProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actionName** | **String** | Gets the job history action name. | [optional] [readonly] 
**endTime** | **Date** | Gets the end time for this job. | [optional] [readonly] 
**expectedExecutionTime** | **Date** | Gets the expected execution time for this job. | [optional] [readonly] 
**message** | **String** | Gets the message for the job history. | [optional] [readonly] 
**repeatCount** | **Number** | Gets the repeat count for the job. | [optional] [readonly] 
**retryCount** | **Number** | Gets the retry count for job. | [optional] [readonly] 
**startTime** | **Date** | Gets the start time for this job. | [optional] [readonly] 
**status** | [**JobExecutionStatus**](JobExecutionStatus.md) |  | [optional] 



## Enum: ActionNameEnum


* `MainAction` (value: `"MainAction"`)

* `ErrorAction` (value: `"ErrorAction"`)




