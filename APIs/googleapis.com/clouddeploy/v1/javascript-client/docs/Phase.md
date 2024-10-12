# CloudDeployApi.Phase

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**childRolloutJobs** | [**ChildRolloutJobs**](ChildRolloutJobs.md) |  | [optional] 
**deploymentJobs** | [**DeploymentJobs**](DeploymentJobs.md) |  | [optional] 
**id** | **String** | Output only. The ID of the Phase. | [optional] [readonly] 
**skipMessage** | **String** | Output only. Additional information on why the Phase was skipped, if available. | [optional] [readonly] 
**state** | **String** | Output only. Current state of the Phase. | [optional] [readonly] 



## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `PENDING` (value: `"PENDING"`)

* `IN_PROGRESS` (value: `"IN_PROGRESS"`)

* `SUCCEEDED` (value: `"SUCCEEDED"`)

* `FAILED` (value: `"FAILED"`)

* `ABORTED` (value: `"ABORTED"`)

* `SKIPPED` (value: `"SKIPPED"`)




