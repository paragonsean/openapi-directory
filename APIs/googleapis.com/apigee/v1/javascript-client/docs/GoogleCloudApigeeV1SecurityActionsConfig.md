# ApigeeApi.GoogleCloudApigeeV1SecurityActionsConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **Boolean** | The flag that controls whether this feature is enabled. This is &#x60;unset&#x60; by default. When this flag is &#x60;false&#x60;, even if individual rules are enabled, no SecurityActions will be enforced. | [optional] 
**name** | **String** | This is a singleton resource, the name will always be set by SecurityActions and any user input will be ignored. The name is always: &#x60;organizations/{org}/environments/{env}/security_actions_config&#x60; | [optional] 
**updateTime** | **String** | Output only. The update time for configuration. | [optional] [readonly] 


