# ConnectorsApi.EventingConfigTemplate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additionalVariables** | [**[ConfigVariableTemplate]**](ConfigVariableTemplate.md) | Additional fields that need to be rendered. | [optional] 
**authConfigTemplates** | [**[AuthConfigTemplate]**](AuthConfigTemplate.md) | AuthConfigTemplates represents the auth values for the webhook adapter. | [optional] 
**autoRefresh** | **Boolean** | Auto refresh to extend webhook life. | [optional] 
**autoRegistrationSupported** | **Boolean** | Auto Registration supported. | [optional] 
**encryptionKeyTemplate** | [**ConfigVariableTemplate**](ConfigVariableTemplate.md) |  | [optional] 
**enrichmentSupported** | **Boolean** | Enrichment Supported. | [optional] 
**eventListenerType** | **String** | The type of the event listener for a specific connector. | [optional] 
**isEventingSupported** | **Boolean** | Is Eventing Supported. | [optional] 
**listenerAuthConfigTemplates** | [**[AuthConfigTemplate]**](AuthConfigTemplate.md) | ListenerAuthConfigTemplates represents the auth values for the event listener. | [optional] 
**proxyDestinationConfig** | [**DestinationConfigTemplate**](DestinationConfigTemplate.md) |  | [optional] 
**registrationDestinationConfig** | [**DestinationConfigTemplate**](DestinationConfigTemplate.md) |  | [optional] 
**triggerConfigVariables** | [**[ConfigVariableTemplate]**](ConfigVariableTemplate.md) | Trigger Config fields that needs to be rendered | [optional] 



## Enum: EventListenerTypeEnum


* `EVENT_LISTENER_TYPE_UNSPECIFIED` (value: `"EVENT_LISTENER_TYPE_UNSPECIFIED"`)

* `WEBHOOK_LISTENER` (value: `"WEBHOOK_LISTENER"`)

* `JMS_LISTENER` (value: `"JMS_LISTENER"`)




