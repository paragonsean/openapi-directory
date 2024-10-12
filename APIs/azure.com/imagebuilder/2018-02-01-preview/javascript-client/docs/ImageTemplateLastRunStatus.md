# VirtualMachineImageTemplate.ImageTemplateLastRunStatus

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endTime** | **Date** | End time of the last run (UTC) | [optional] 
**message** | **String** | Verbose information about the last run state | [optional] 
**runState** | **String** | State of the last run | [optional] 
**runSubState** | **String** | Sub state of the last run | [optional] 
**startTime** | **Date** | Start time of the last run (UTC) | [optional] 



## Enum: RunStateEnum


* `ready` (value: `"ready"`)

* `running` (value: `"running"`)

* `succeeded` (value: `"succeeded"`)

* `partiallySucceeded` (value: `"partiallySucceeded"`)

* `failed` (value: `"failed"`)





## Enum: RunSubStateEnum


* `queued` (value: `"queued"`)

* `building` (value: `"building"`)

* `customizing` (value: `"customizing"`)

* `distributing` (value: `"distributing"`)




