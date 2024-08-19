# GitHubV3RestApi.DeploymentStatus

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createdAt** | **Date** |  | 
**creator** | [**NullableSimpleUser**](NullableSimpleUser.md) |  | 
**deploymentUrl** | **String** |  | 
**description** | **String** | A short description of the status. | [default to &#39;&#39;]
**environment** | **String** | The environment of the deployment that the status is for. | [optional] [default to &#39;&#39;]
**environmentUrl** | **String** | The URL for accessing your environment. | [optional] [default to &#39;&#39;]
**id** | **Number** |  | 
**logUrl** | **String** | The URL to associate with this status. | [optional] [default to &#39;&#39;]
**nodeId** | **String** |  | 
**performedViaGithubApp** | [**NullableIntegration**](NullableIntegration.md) |  | [optional] 
**repositoryUrl** | **String** |  | 
**state** | **String** | The state of the status. | 
**targetUrl** | **String** | Deprecated: the URL to associate with this status. | [default to &#39;&#39;]
**updatedAt** | **Date** |  | 
**url** | **String** |  | 



## Enum: StateEnum


* `error` (value: `"error"`)

* `failure` (value: `"failure"`)

* `inactive` (value: `"inactive"`)

* `pending` (value: `"pending"`)

* `success` (value: `"success"`)

* `queued` (value: `"queued"`)

* `in_progress` (value: `"in_progress"`)




