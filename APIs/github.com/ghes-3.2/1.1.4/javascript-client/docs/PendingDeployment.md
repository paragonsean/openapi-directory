# GitHubV3RestApi.PendingDeployment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currentUserCanApprove** | **Boolean** | Whether the currently authenticated user can approve the deployment | 
**environment** | [**PendingDeploymentEnvironment**](PendingDeploymentEnvironment.md) |  | 
**reviewers** | [**[EnvironmentProtectionRulesInnerAnyOf1ReviewersInner]**](EnvironmentProtectionRulesInnerAnyOf1ReviewersInner.md) | The people or teams that may approve jobs that reference the environment. You can list up to six users or teams as reviewers. The reviewers must have at least read access to the repository. Only one of the required reviewers needs to approve the job for it to proceed. | 
**waitTimer** | **Number** | The set duration of the wait timer | 
**waitTimerStartedAt** | **Date** | The time that the wait timer began. | 


