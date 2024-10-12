

# CreateDeploymentJobRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**deploymentConfig** | [**CreateDeploymentJobRequestDeploymentConfig**](CreateDeploymentJobRequestDeploymentConfig.md) |  |  [optional] |
|**clientRequestToken** | **String** | Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. |  |
|**fleet** | **String** | The Amazon Resource Name (ARN) of the fleet to deploy. |  |
|**deploymentApplicationConfigs** | [**List&lt;DeploymentApplicationConfig&gt;**](DeploymentApplicationConfig.md) | The deployment application configuration. |  |
|**tags** | **Map&lt;String, String&gt;** | A map that contains tag keys and tag values that are attached to the deployment job. |  [optional] |



