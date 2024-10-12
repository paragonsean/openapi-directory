

# RoutesConfigDump

Envoy's RDS implementation fills this message with all currently loaded routes, as described by their RouteConfiguration objects. Static routes that are either defined in the bootstrap configuration or defined inline while configuring listeners are separated from those configured dynamically via RDS. Route configuration information can be used to recreate an Envoy configuration by populating all routes as static routes or by returning them in RDS responses.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dynamicRouteConfigs** | [**List&lt;DynamicRouteConfig&gt;**](DynamicRouteConfig.md) | The dynamically loaded route configs. |  [optional] |
|**staticRouteConfigs** | [**List&lt;StaticRouteConfig&gt;**](StaticRouteConfig.md) | The statically loaded route configs. |  [optional] |



