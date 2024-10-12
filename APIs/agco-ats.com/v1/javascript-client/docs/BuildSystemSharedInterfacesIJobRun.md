# AgcoApi.BuildSystemSharedInterfacesIJobRun

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activityRuns** | [**[BuildSystemSharedInterfacesIActivityRun]**](BuildSystemSharedInterfacesIActivityRun.md) | ActivityRuns | [optional] 
**endDate** | **Date** | end date | [optional] 
**jobID** | **Number** | job id | [optional] 
**jobRunID** | **Number** | JobRunID | [optional] [readonly] 
**parameters** | [**[BuildSystemSharedInterfacesIParameterValue]**](BuildSystemSharedInterfacesIParameterValue.md) | Parameters | [optional] [readonly] 
**startDate** | **Date** | Start Date | [optional] 
**status** | **String** | status | [optional] 



## Enum: StatusEnum


* `Ready` (value: `"Ready"`)

* `InProgress` (value: `"InProgress"`)

* `Succeeded` (value: `"Succeeded"`)

* `Cancelled` (value: `"Cancelled"`)

* `Failed` (value: `"Failed"`)




