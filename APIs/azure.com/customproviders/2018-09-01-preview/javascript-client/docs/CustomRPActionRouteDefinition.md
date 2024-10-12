# Customproviders.CustomRPActionRouteDefinition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**routingType** | **String** | The routing types that are supported for action requests. | [optional] 
**endpoint** | **String** | The route definition endpoint URI that the custom resource provider will proxy requests to. This can be in the form of a flat URI (e.g. &#39;https://testendpoint/&#39;) or can specify to route via a path (e.g. &#39;https://testendpoint/{requestPath}&#39;) | 
**name** | **String** | The name of the route definition. This becomes the name for the ARM extension (e.g. &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CustomProviders/resourceProviders/{resourceProviderName}/{name}&#39;) | 



## Enum: RoutingTypeEnum


* `Proxy` (value: `"Proxy"`)




