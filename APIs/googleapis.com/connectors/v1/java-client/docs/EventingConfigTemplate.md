

# EventingConfigTemplate

Eventing Config details of a connector version.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**additionalVariables** | [**List&lt;ConfigVariableTemplate&gt;**](ConfigVariableTemplate.md) | Additional fields that need to be rendered. |  [optional] |
|**authConfigTemplates** | [**List&lt;AuthConfigTemplate&gt;**](AuthConfigTemplate.md) | AuthConfigTemplates represents the auth values for the webhook adapter. |  [optional] |
|**autoRefresh** | **Boolean** | Auto refresh to extend webhook life. |  [optional] |
|**autoRegistrationSupported** | **Boolean** | Auto Registration supported. |  [optional] |
|**encryptionKeyTemplate** | [**ConfigVariableTemplate**](ConfigVariableTemplate.md) |  |  [optional] |
|**enrichmentSupported** | **Boolean** | Enrichment Supported. |  [optional] |
|**eventListenerType** | [**EventListenerTypeEnum**](#EventListenerTypeEnum) | The type of the event listener for a specific connector. |  [optional] |
|**isEventingSupported** | **Boolean** | Is Eventing Supported. |  [optional] |
|**listenerAuthConfigTemplates** | [**List&lt;AuthConfigTemplate&gt;**](AuthConfigTemplate.md) | ListenerAuthConfigTemplates represents the auth values for the event listener. |  [optional] |
|**proxyDestinationConfig** | [**DestinationConfigTemplate**](DestinationConfigTemplate.md) |  |  [optional] |
|**registrationDestinationConfig** | [**DestinationConfigTemplate**](DestinationConfigTemplate.md) |  |  [optional] |
|**triggerConfigVariables** | [**List&lt;ConfigVariableTemplate&gt;**](ConfigVariableTemplate.md) | Trigger Config fields that needs to be rendered |  [optional] |



## Enum: EventListenerTypeEnum

| Name | Value |
|---- | -----|
| EVENT_LISTENER_TYPE_UNSPECIFIED | &quot;EVENT_LISTENER_TYPE_UNSPECIFIED&quot; |
| WEBHOOK_LISTENER | &quot;WEBHOOK_LISTENER&quot; |
| JMS_LISTENER | &quot;JMS_LISTENER&quot; |



