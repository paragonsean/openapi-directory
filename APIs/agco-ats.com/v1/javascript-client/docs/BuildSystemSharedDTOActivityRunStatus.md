# AgcoApi.BuildSystemSharedDTOActivityRunStatus

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currentStep** | **Number** | The activity step currently executing, indicated by numeric order | [optional] 
**status** | **String** | The status of the ActivityRun | [optional] 
**stepProgress** | **Number** | The percent progress from the currently executing step.  This value shall be null if progress is not available | [optional] 
**stepStatus** | **String** | The status text from the currently executing step | [optional] 



## Enum: StatusEnum


* `Ready` (value: `"Ready"`)

* `InProgress` (value: `"InProgress"`)

* `Succeeded` (value: `"Succeeded"`)

* `Cancelled` (value: `"Cancelled"`)

* `Failed` (value: `"Failed"`)




