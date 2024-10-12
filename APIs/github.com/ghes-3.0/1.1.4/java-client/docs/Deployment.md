

# Deployment

A request for a specific ref(branch,sha,tag) to be deployed

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdAt** | **OffsetDateTime** |  |  |
|**creator** | [**NullableSimpleUser**](NullableSimpleUser.md) |  |  |
|**description** | **String** |  |  |
|**environment** | **String** | Name for the target deployment environment. |  |
|**id** | **Integer** | Unique identifier of the deployment |  |
|**nodeId** | **String** |  |  |
|**originalEnvironment** | **String** |  |  [optional] |
|**payload** | [**DeploymentPayload**](DeploymentPayload.md) |  |  |
|**performedViaGithubApp** | [**NullableIntegration**](NullableIntegration.md) |  |  [optional] |
|**productionEnvironment** | **Boolean** | Specifies if the given environment is one that end-users directly interact with. Default: false. |  [optional] |
|**ref** | **String** | The ref to deploy. This can be a branch, tag, or sha. |  |
|**repositoryUrl** | **URI** |  |  |
|**sha** | **String** |  |  |
|**statusesUrl** | **URI** |  |  |
|**task** | **String** | Parameter to specify a task to execute |  |
|**transientEnvironment** | **Boolean** | Specifies if the given environment is will no longer exist at some point in the future. Default: false. |  [optional] |
|**updatedAt** | **OffsetDateTime** |  |  |
|**url** | **URI** |  |  |



