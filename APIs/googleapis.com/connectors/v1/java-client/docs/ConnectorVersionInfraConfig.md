

# ConnectorVersionInfraConfig

This cofiguration provides infra configs like rate limit threshold which need to be configurable for every connector version

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**connectionRatelimitWindowSeconds** | **String** | Output only. The window used for ratelimiting runtime requests to connections. |  [optional] [readonly] |
|**deploymentModel** | [**DeploymentModelEnum**](#DeploymentModelEnum) | Optional. Indicates whether connector is deployed on GKE/CloudRun |  [optional] |
|**hpaConfig** | [**HPAConfig**](HPAConfig.md) |  |  [optional] |
|**internalclientRatelimitThreshold** | **String** | Output only. Max QPS supported for internal requests originating from Connd. |  [optional] [readonly] |
|**ratelimitThreshold** | **String** | Output only. Max QPS supported by the connector version before throttling of requests. |  [optional] [readonly] |
|**resourceLimits** | [**ResourceLimits**](ResourceLimits.md) |  |  [optional] |
|**resourceRequests** | [**ResourceRequests**](ResourceRequests.md) |  |  [optional] |
|**sharedDeployment** | **String** | Output only. The name of shared connector deployment. |  [optional] [readonly] |



## Enum: DeploymentModelEnum

| Name | Value |
|---- | -----|
| DEPLOYMENT_MODEL_UNSPECIFIED | &quot;DEPLOYMENT_MODEL_UNSPECIFIED&quot; |
| GKE_MST | &quot;GKE_MST&quot; |
| CLOUD_RUN_MST | &quot;CLOUD_RUN_MST&quot; |



