# AgcoApi.BuildSystemSharedDTOJobRun

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activityRuns** | [**[BuildSystemSharedDTOActivityRun]**](BuildSystemSharedDTOActivityRun.md) | The activity runs belonging to this JobRun | [optional] [readonly] 
**endDate** | **Date** | The UTC date and time when the job completed | [optional] 
**jobID** | **Number** | The ID of the job that defines the run | [optional] 
**jobRunID** | **Number** | The ID of this JobRun | [optional] 
**parameters** | [**[BuildSystemSharedDTOParameterValue]**](BuildSystemSharedDTOParameterValue.md) | The parameters used for this run of the job | [optional] [readonly] 
**startDate** | **Date** | The UTC date and time when the job started | [optional] 
**status** | **String** | The status of this JobRun | [optional] 



## Enum: StatusEnum


* `Ready` (value: `"Ready"`)

* `InProgress` (value: `"InProgress"`)

* `Succeeded` (value: `"Succeeded"`)

* `Cancelled` (value: `"Cancelled"`)

* `Failed` (value: `"Failed"`)




