# CloudRuntimeConfigurationApi.RuntimeConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **String** | An optional description of the RuntimeConfig object. | [optional] 
**name** | **String** | The resource name of a runtime config. The name must have the format: projects/[PROJECT_ID]/configs/[CONFIG_NAME] The &#x60;[PROJECT_ID]&#x60; must be a valid project ID, and &#x60;[CONFIG_NAME]&#x60; is an arbitrary name that matches the &#x60;[0-9A-Za-z](?:[_.A-Za-z0-9-]{0,62}[_.A-Za-z0-9])?&#x60; regular expression. The length of &#x60;[CONFIG_NAME]&#x60; must be less than 64 characters. You pick the RuntimeConfig resource name, but the server will validate that the name adheres to this format. After you create the resource, you cannot change the resource&#39;s name. | [optional] 


