

# DeploymentSimple

A deployment created as the result of an Actions check run from a workflow that references an environment

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdAt** | **OffsetDateTime** |  |  |
|**description** | **String** |  |  |
|**environment** | **String** | Name for the target deployment environment. |  |
|**id** | **Integer** | Unique identifier of the deployment |  |
|**nodeId** | **String** |  |  |
|**originalEnvironment** | **String** |  |  [optional] |
|**performedViaGithubApp** | [**NullableIntegration**](NullableIntegration.md) |  |  [optional] |
|**productionEnvironment** | **Boolean** | Specifies if the given environment is one that end-users directly interact with. Default: false. |  [optional] |
|**repositoryUrl** | **URI** |  |  |
|**statusesUrl** | **URI** |  |  |
|**task** | **String** | Parameter to specify a task to execute |  |
|**transientEnvironment** | **Boolean** | Specifies if the given environment is will no longer exist at some point in the future. Default: false. |  [optional] |
|**updatedAt** | **OffsetDateTime** |  |  |
|**url** | **URI** |  |  |



