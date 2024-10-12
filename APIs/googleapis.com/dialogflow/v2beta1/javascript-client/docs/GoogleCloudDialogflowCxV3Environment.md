# DialogflowApi.GoogleCloudDialogflowCxV3Environment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **String** | The human-readable description of the environment. The maximum length is 500 characters. If exceeded, the request is rejected. | [optional] 
**displayName** | **String** | Required. The human-readable name of the environment (unique in an agent). Limit of 64 characters. | [optional] 
**name** | **String** | The name of the environment. Format: &#x60;projects//locations//agents//environments/&#x60;. | [optional] 
**testCasesConfig** | [**GoogleCloudDialogflowCxV3EnvironmentTestCasesConfig**](GoogleCloudDialogflowCxV3EnvironmentTestCasesConfig.md) |  | [optional] 
**updateTime** | **String** | Output only. Update time of this environment. | [optional] [readonly] 
**versionConfigs** | [**[GoogleCloudDialogflowCxV3EnvironmentVersionConfig]**](GoogleCloudDialogflowCxV3EnvironmentVersionConfig.md) | A list of configurations for flow versions. You should include version configs for all flows that are reachable from &#x60;Start Flow&#x60; in the agent. Otherwise, an error will be returned. | [optional] 
**webhookConfig** | [**GoogleCloudDialogflowCxV3EnvironmentWebhookConfig**](GoogleCloudDialogflowCxV3EnvironmentWebhookConfig.md) |  | [optional] 


