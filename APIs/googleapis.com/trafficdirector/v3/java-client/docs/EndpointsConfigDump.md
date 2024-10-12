

# EndpointsConfigDump

Envoy's admin fill this message with all currently known endpoints. Endpoint configuration information can be used to recreate an Envoy configuration by populating all endpoints as static endpoints or by returning them in an EDS response.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dynamicEndpointConfigs** | [**List&lt;DynamicEndpointConfig&gt;**](DynamicEndpointConfig.md) | The dynamically loaded endpoint configs. |  [optional] |
|**staticEndpointConfigs** | [**List&lt;StaticEndpointConfig&gt;**](StaticEndpointConfig.md) | The statically loaded endpoint configs. |  [optional] |



