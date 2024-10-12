# GitHubV3RestApi.EnvironmentApprovals

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **String** | The comment submitted with the deployment review | 
**environments** | [**[EnvironmentApprovalsEnvironmentsInner]**](EnvironmentApprovalsEnvironmentsInner.md) | The list of environments that were approved or rejected | 
**state** | **String** | Whether deployment to the environment(s) was approved or rejected | 
**user** | [**SimpleUser**](SimpleUser.md) |  | 



## Enum: StateEnum


* `approved` (value: `"approved"`)

* `rejected` (value: `"rejected"`)




