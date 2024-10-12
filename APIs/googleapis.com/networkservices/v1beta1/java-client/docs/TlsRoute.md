

# TlsRoute

TlsRoute defines how traffic should be routed based on SNI and other matching L3 attributes.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | Output only. The timestamp when the resource was created. |  [optional] [readonly] |
|**description** | **String** | Optional. A free-text description of the resource. Max length 1024 characters. |  [optional] |
|**gateways** | **List&lt;String&gt;** | Optional. Gateways defines a list of gateways this TlsRoute is attached to, as one of the routing rules to route the requests served by the gateway. Each gateway reference should match the pattern: &#x60;projects/_*_/locations/global/gateways/&#x60; |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | Optional. Set of label tags associated with the TlsRoute resource. |  [optional] |
|**meshes** | **List&lt;String&gt;** | Optional. Meshes defines a list of meshes this TlsRoute is attached to, as one of the routing rules to route the requests served by the mesh. Each mesh reference should match the pattern: &#x60;projects/_*_/locations/global/meshes/&#x60; The attached Mesh should be of a type SIDECAR |  [optional] |
|**name** | **String** | Required. Name of the TlsRoute resource. It matches pattern &#x60;projects/_*_/locations/global/tlsRoutes/tls_route_name&gt;&#x60;. |  [optional] |
|**rules** | [**List&lt;TlsRouteRouteRule&gt;**](TlsRouteRouteRule.md) | Required. Rules that define how traffic is routed and handled. At least one RouteRule must be supplied. If there are multiple rules then the action taken will be the first rule to match. |  [optional] |
|**selfLink** | **String** | Output only. Server-defined URL of this resource |  [optional] [readonly] |
|**updateTime** | **String** | Output only. The timestamp when the resource was updated. |  [optional] [readonly] |



