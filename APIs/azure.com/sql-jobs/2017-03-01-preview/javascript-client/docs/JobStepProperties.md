# SqlManagementClient.JobStepProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | [**JobStepAction**](JobStepAction.md) |  | 
**credential** | **String** | The resource ID of the job credential that will be used to connect to the targets. | 
**executionOptions** | [**JobStepExecutionOptions**](JobStepExecutionOptions.md) |  | [optional] 
**output** | [**JobStepOutput**](JobStepOutput.md) |  | [optional] 
**stepId** | **Number** | The job step&#39;s index within the job. If not specified when creating the job step, it will be created as the last step. If not specified when updating the job step, the step id is not modified. | [optional] 
**targetGroup** | **String** | The resource ID of the target group that the job step will be executed on. | 


