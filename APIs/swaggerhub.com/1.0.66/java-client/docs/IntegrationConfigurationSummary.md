

# IntegrationConfigurationSummary


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**enabled** | **Boolean** | Whether the integration is enabled or disabled |  [optional] |
|**id** | **UUID** | ID of the integration |  [optional] [readonly] |
|**name** | **String** | The display name of the integration. Must be unique among all integrations configured for the given API version. |  |
|**configType** | [**ConfigTypeEnum**](#ConfigTypeEnum) | Integration type |  |



## Enum: ConfigTypeEnum

| Name | Value |
|---- | -----|
| AMAZON_API_GATEWAY | &quot;AMAZON_API_GATEWAY&quot; |
| AMAZON_API_GATEWAY_LAMBDA | &quot;AMAZON_API_GATEWAY_LAMBDA&quot; |
| API_AUTO_MOCKING | &quot;API_AUTO_MOCKING&quot; |
| APIGEE_EDGE | &quot;APIGEE_EDGE&quot; |
| AZURE_DEVOPS_SERVICES | &quot;AZURE_DEVOPS_SERVICES&quot; |
| BITBUCKET_CLOUD | &quot;BITBUCKET_CLOUD&quot; |
| BITBUCKET_SERVER | &quot;BITBUCKET_SERVER&quot; |
| GITHUB | &quot;GITHUB&quot; |
| GITHUB_ENTERPRISE | &quot;GITHUB_ENTERPRISE&quot; |
| GITLAB | &quot;GITLAB&quot; |
| WEBHOOK | &quot;WEBHOOK&quot; |



