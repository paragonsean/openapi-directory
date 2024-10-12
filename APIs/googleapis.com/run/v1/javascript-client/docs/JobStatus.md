# CloudRunAdminApi.JobStatus

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditions** | [**[GoogleCloudRunV1Condition]**](GoogleCloudRunV1Condition.md) | Conditions communicate information about ongoing/complete reconciliation processes that bring the \&quot;spec\&quot; inline with the observed state of the world. Job-specific conditions include: * &#x60;Ready&#x60;: &#x60;True&#x60; when the job is ready to be executed. | [optional] 
**executionCount** | **Number** | Number of executions created for this job. | [optional] 
**latestCreatedExecution** | [**ExecutionReference**](ExecutionReference.md) |  | [optional] 
**observedGeneration** | **Number** | The &#39;generation&#39; of the job that was last processed by the controller. | [optional] 


