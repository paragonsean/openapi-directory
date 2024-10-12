# ConnectorsApi.ConnectorInfraConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connectionRatelimitWindowSeconds** | **String** | The window used for ratelimiting runtime requests to connections. | [optional] 
**deploymentModel** | **String** | Indicate whether connector is deployed on GKE/CloudRun | [optional] 
**hpaConfig** | [**HPAConfig**](HPAConfig.md) |  | [optional] 
**internalclientRatelimitThreshold** | **String** | Max QPS supported for internal requests originating from Connd. | [optional] 
**ratelimitThreshold** | **String** | Max QPS supported by the connector version before throttling of requests. | [optional] 
**resourceLimits** | [**ResourceLimits**](ResourceLimits.md) |  | [optional] 
**resourceRequests** | [**ResourceRequests**](ResourceRequests.md) |  | [optional] 
**sharedDeployment** | **String** | The name of shared connector deployment. | [optional] 



## Enum: DeploymentModelEnum


* `DEPLOYMENT_MODEL_UNSPECIFIED` (value: `"DEPLOYMENT_MODEL_UNSPECIFIED"`)

* `GKE_MST` (value: `"GKE_MST"`)

* `CLOUD_RUN_MST` (value: `"CLOUD_RUN_MST"`)




