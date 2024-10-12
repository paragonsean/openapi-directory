# ConnectorApi.ConnectorUnifiedApisInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authOnly** | **Boolean** | Indicates whether a connector only supports authentication. In this case the connector is not mapped to a Unified API, but can be used with the Proxy API | [optional] [readonly] 
**downstreamUnsupportedResources** | **[String]** | List of resources that are not supported on the downstream. | [optional] 
**id** | [**UnifiedApiId**](UnifiedApiId.md) |  | [optional] 
**name** | **String** | Name of the API. | [optional] 
**oauthScopes** | [**[ConnectorUnifiedApisInnerOauthScopesInner]**](ConnectorUnifiedApisInnerOauthScopesInner.md) |  | [optional] 
**supportedEvents** | [**[ConnectorEvent]**](ConnectorEvent.md) | List of events that are supported on the connector for this Unified API. | [optional] 
**supportedResources** | [**[LinkedConnectorResource]**](LinkedConnectorResource.md) | List of resources that are supported on the connector. | [optional] 


