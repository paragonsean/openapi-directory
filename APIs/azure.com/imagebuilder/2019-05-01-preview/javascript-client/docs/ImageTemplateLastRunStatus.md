# VirtualMachineImageTemplate.ImageTemplateLastRunStatus

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endTime** | **Date** | End time of the last run (UTC) | [optional] 
**message** | **String** | Verbose information about the last run state | [optional] 
**runState** | **String** | State of the last run | [optional] 
**runSubState** | **String** | Sub-state of the last run | [optional] 
**startTime** | **Date** | Start time of the last run (UTC) | [optional] 



## Enum: RunStateEnum


* `Running` (value: `"Running"`)

* `Succeeded` (value: `"Succeeded"`)

* `PartiallySucceeded` (value: `"PartiallySucceeded"`)

* `Failed` (value: `"Failed"`)





## Enum: RunSubStateEnum


* `Queued` (value: `"Queued"`)

* `Building` (value: `"Building"`)

* `Customizing` (value: `"Customizing"`)

* `Distributing` (value: `"Distributing"`)




