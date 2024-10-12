# CloudTasksApi.TaskStatus

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attemptDispatchCount** | **Number** | Output only. The number of attempts dispatched. This count includes attempts which have been dispatched but haven&#39;t received a response. | [optional] 
**attemptResponseCount** | **Number** | Output only. The number of attempts which have received a response. This field is not calculated for pull tasks. | [optional] 
**firstAttemptStatus** | [**AttemptStatus**](AttemptStatus.md) |  | [optional] 
**lastAttemptStatus** | [**AttemptStatus**](AttemptStatus.md) |  | [optional] 


