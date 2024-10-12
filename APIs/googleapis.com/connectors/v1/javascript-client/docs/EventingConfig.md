# ConnectorsApi.EventingConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additionalVariables** | [**[ConfigVariable]**](ConfigVariable.md) | Additional eventing related field values | [optional] 
**authConfig** | [**AuthConfig**](AuthConfig.md) |  | [optional] 
**deadLetterConfig** | [**DeadLetterConfig**](DeadLetterConfig.md) |  | [optional] 
**enrichmentEnabled** | **Boolean** | Enrichment Enabled. | [optional] 
**eventsListenerIngressEndpoint** | **String** | Optional. Ingress endpoint of the event listener. This is used only when private connectivity is enabled. | [optional] 
**listenerAuthConfig** | [**AuthConfig**](AuthConfig.md) |  | [optional] 
**privateConnectivityEnabled** | **Boolean** | Optional. Private Connectivity Enabled. | [optional] 
**proxyDestinationConfig** | [**DestinationConfig**](DestinationConfig.md) |  | [optional] 
**registrationDestinationConfig** | [**DestinationConfig**](DestinationConfig.md) |  | [optional] 
**triggerConfigVariables** | [**[ConfigVariable]**](ConfigVariable.md) | Optional. Additional eventing related field values | [optional] 


