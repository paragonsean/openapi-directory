

# ScopedRoutesConfigDump

Envoy's scoped RDS implementation fills this message with all currently loaded route configuration scopes (defined via ScopedRouteConfigurationsSet protos). This message lists both the scopes defined inline with the higher order object (i.e., the HttpConnectionManager) and the dynamically obtained scopes via the SRDS API.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dynamicScopedRouteConfigs** | [**List&lt;DynamicScopedRouteConfigs&gt;**](DynamicScopedRouteConfigs.md) | The dynamically loaded scoped route configs. |  [optional] |
|**inlineScopedRouteConfigs** | [**List&lt;InlineScopedRouteConfigs&gt;**](InlineScopedRouteConfigs.md) | The statically loaded scoped route configs. |  [optional] |



