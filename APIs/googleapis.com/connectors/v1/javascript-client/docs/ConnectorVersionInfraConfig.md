# ConnectorsApi.ConnectorVersionInfraConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connectionRatelimitWindowSeconds** | **String** | Output only. The window used for ratelimiting runtime requests to connections. | [optional] [readonly] 
**deploymentModel** | **String** | Optional. Indicates whether connector is deployed on GKE/CloudRun | [optional] 
**hpaConfig** | [**HPAConfig**](HPAConfig.md) |  | [optional] 
**internalclientRatelimitThreshold** | **String** | Output only. Max QPS supported for internal requests originating from Connd. | [optional] [readonly] 
**ratelimitThreshold** | **String** | Output only. Max QPS supported by the connector version before throttling of requests. | [optional] [readonly] 
**resourceLimits** | [**ResourceLimits**](ResourceLimits.md) |  | [optional] 
**resourceRequests** | [**ResourceRequests**](ResourceRequests.md) |  | [optional] 
**sharedDeployment** | **String** | Output only. The name of shared connector deployment. | [optional] [readonly] 



## Enum: DeploymentModelEnum


* `DEPLOYMENT_MODEL_UNSPECIFIED` (value: `"DEPLOYMENT_MODEL_UNSPECIFIED"`)

* `GKE_MST` (value: `"GKE_MST"`)

* `CLOUD_RUN_MST` (value: `"CLOUD_RUN_MST"`)




