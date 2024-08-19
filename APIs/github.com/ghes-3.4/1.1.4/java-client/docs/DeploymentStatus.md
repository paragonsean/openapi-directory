

# DeploymentStatus

The status of a deployment.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdAt** | **OffsetDateTime** |  |  |
|**creator** | [**NullableSimpleUser**](NullableSimpleUser.md) |  |  |
|**deploymentUrl** | **URI** |  |  |
|**description** | **String** | A short description of the status. |  |
|**environment** | **String** | The environment of the deployment that the status is for. |  [optional] |
|**environmentUrl** | **URI** | The URL for accessing your environment. |  [optional] |
|**id** | **Integer** |  |  |
|**logUrl** | **URI** | The URL to associate with this status. |  [optional] |
|**nodeId** | **String** |  |  |
|**performedViaGithubApp** | [**NullableIntegration**](NullableIntegration.md) |  |  [optional] |
|**repositoryUrl** | **URI** |  |  |
|**state** | [**StateEnum**](#StateEnum) | The state of the status. |  |
|**targetUrl** | **URI** | Deprecated: the URL to associate with this status. |  |
|**updatedAt** | **OffsetDateTime** |  |  |
|**url** | **URI** |  |  |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| ERROR | &quot;error&quot; |
| FAILURE | &quot;failure&quot; |
| INACTIVE | &quot;inactive&quot; |
| PENDING | &quot;pending&quot; |
| SUCCESS | &quot;success&quot; |
| QUEUED | &quot;queued&quot; |
| IN_PROGRESS | &quot;in_progress&quot; |



