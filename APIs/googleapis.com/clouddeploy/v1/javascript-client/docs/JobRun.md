# CloudDeployApi.JobRun

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advanceChildRolloutJobRun** | [**AdvanceChildRolloutJobRun**](AdvanceChildRolloutJobRun.md) |  | [optional] 
**createChildRolloutJobRun** | [**CreateChildRolloutJobRun**](CreateChildRolloutJobRun.md) |  | [optional] 
**createTime** | **String** | Output only. Time at which the &#x60;JobRun&#x60; was created. | [optional] [readonly] 
**deployJobRun** | [**DeployJobRun**](DeployJobRun.md) |  | [optional] 
**endTime** | **String** | Output only. Time at which the &#x60;JobRun&#x60; ended. | [optional] [readonly] 
**etag** | **String** | Output only. This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. | [optional] [readonly] 
**jobId** | **String** | Output only. ID of the &#x60;Rollout&#x60; job this &#x60;JobRun&#x60; corresponds to. | [optional] [readonly] 
**name** | **String** | Optional. Name of the &#x60;JobRun&#x60;. Format is &#x60;projects/{project}/locations/{location}/deliveryPipelines/{deliveryPipeline}/releases/{releases}/rollouts/{rollouts}/jobRuns/{uuid}&#x60;. | [optional] 
**phaseId** | **String** | Output only. ID of the &#x60;Rollout&#x60; phase this &#x60;JobRun&#x60; belongs in. | [optional] [readonly] 
**postdeployJobRun** | [**PostdeployJobRun**](PostdeployJobRun.md) |  | [optional] 
**predeployJobRun** | [**PredeployJobRun**](PredeployJobRun.md) |  | [optional] 
**startTime** | **String** | Output only. Time at which the &#x60;JobRun&#x60; was started. | [optional] [readonly] 
**state** | **String** | Output only. The current state of the &#x60;JobRun&#x60;. | [optional] [readonly] 
**uid** | **String** | Output only. Unique identifier of the &#x60;JobRun&#x60;. | [optional] [readonly] 
**verifyJobRun** | [**VerifyJobRun**](VerifyJobRun.md) |  | [optional] 



## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `IN_PROGRESS` (value: `"IN_PROGRESS"`)

* `SUCCEEDED` (value: `"SUCCEEDED"`)

* `FAILED` (value: `"FAILED"`)

* `TERMINATING` (value: `"TERMINATING"`)

* `TERMINATED` (value: `"TERMINATED"`)




