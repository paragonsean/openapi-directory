

# ConnectorUnifiedApisInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**authOnly** | **Boolean** | Indicates whether a connector only supports authentication. In this case the connector is not mapped to a Unified API, but can be used with the Proxy API |  [optional] [readonly] |
|**downstreamUnsupportedResources** | **List&lt;String&gt;** | List of resources that are not supported on the downstream. |  [optional] |
|**id** | **UnifiedApiId** |  |  [optional] |
|**name** | **String** | Name of the API. |  [optional] |
|**oauthScopes** | [**List&lt;ConnectorUnifiedApisInnerOauthScopesInner&gt;**](ConnectorUnifiedApisInnerOauthScopesInner.md) |  |  [optional] |
|**supportedEvents** | [**List&lt;ConnectorEvent&gt;**](ConnectorEvent.md) | List of events that are supported on the connector for this Unified API. |  [optional] |
|**supportedResources** | [**List&lt;LinkedConnectorResource&gt;**](LinkedConnectorResource.md) | List of resources that are supported on the connector. |  [optional] |



