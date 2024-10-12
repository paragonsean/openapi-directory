

# GoogleCloudDialogflowCxV3beta1Deployment

Represents a deployment in an environment. A deployment happens when a flow version configured to be active in the environment. You can configure running pre-deployment steps, e.g. running validation test cases, experiment auto-rollout, etc.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**endTime** | **String** | End time of this deployment. |  [optional] |
|**flowVersion** | **String** | The name of the flow version for this deployment. Format: projects//locations//agents//flows//versions/. |  [optional] |
|**name** | **String** | The name of the deployment. Format: projects//locations//agents//environments//deployments/. |  [optional] |
|**result** | [**GoogleCloudDialogflowCxV3beta1DeploymentResult**](GoogleCloudDialogflowCxV3beta1DeploymentResult.md) |  |  [optional] |
|**startTime** | **String** | Start time of this deployment. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | The current state of the deployment. |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| RUNNING | &quot;RUNNING&quot; |
| SUCCEEDED | &quot;SUCCEEDED&quot; |
| FAILED | &quot;FAILED&quot; |



