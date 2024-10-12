# GitHubV3RestApi.Deployment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createdAt** | **Date** |  | 
**creator** | [**NullableSimpleUser**](NullableSimpleUser.md) |  | 
**description** | **String** |  | 
**environment** | **String** | Name for the target deployment environment. | 
**id** | **Number** | Unique identifier of the deployment | 
**nodeId** | **String** |  | 
**originalEnvironment** | **String** |  | [optional] 
**payload** | [**DeploymentPayload**](DeploymentPayload.md) |  | 
**performedViaGithubApp** | [**NullableIntegration**](NullableIntegration.md) |  | [optional] 
**productionEnvironment** | **Boolean** | Specifies if the given environment is one that end-users directly interact with. Default: false. | [optional] 
**ref** | **String** | The ref to deploy. This can be a branch, tag, or sha. | 
**repositoryUrl** | **String** |  | 
**sha** | **String** |  | 
**statusesUrl** | **String** |  | 
**task** | **String** | Parameter to specify a task to execute | 
**transientEnvironment** | **Boolean** | Specifies if the given environment is will no longer exist at some point in the future. Default: false. | [optional] 
**updatedAt** | **Date** |  | 
**url** | **String** |  | 


