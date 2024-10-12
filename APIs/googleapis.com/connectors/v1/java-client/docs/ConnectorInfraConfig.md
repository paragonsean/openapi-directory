

# ConnectorInfraConfig

This cofiguration provides infra configs like rate limit threshold which need to be configurable for every connector version

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**connectionRatelimitWindowSeconds** | **String** | The window used for ratelimiting runtime requests to connections. |  [optional] |
|**deploymentModel** | [**DeploymentModelEnum**](#DeploymentModelEnum) | Indicate whether connector is deployed on GKE/CloudRun |  [optional] |
|**hpaConfig** | [**HPAConfig**](HPAConfig.md) |  |  [optional] |
|**internalclientRatelimitThreshold** | **String** | Max QPS supported for internal requests originating from Connd. |  [optional] |
|**ratelimitThreshold** | **String** | Max QPS supported by the connector version before throttling of requests. |  [optional] |
|**resourceLimits** | [**ResourceLimits**](ResourceLimits.md) |  |  [optional] |
|**resourceRequests** | [**ResourceRequests**](ResourceRequests.md) |  |  [optional] |
|**sharedDeployment** | **String** | The name of shared connector deployment. |  [optional] |



## Enum: DeploymentModelEnum

| Name | Value |
|---- | -----|
| DEPLOYMENT_MODEL_UNSPECIFIED | &quot;DEPLOYMENT_MODEL_UNSPECIFIED&quot; |
| GKE_MST | &quot;GKE_MST&quot; |
| CLOUD_RUN_MST | &quot;CLOUD_RUN_MST&quot; |



