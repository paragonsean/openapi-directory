

# HttpRoute

HttpRoute is the resource defining how HTTP traffic should be routed by a Mesh or Gateway resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | Output only. The timestamp when the resource was created. |  [optional] [readonly] |
|**description** | **String** | Optional. A free-text description of the resource. Max length 1024 characters. |  [optional] |
|**gateways** | **List&lt;String&gt;** | Optional. Gateways defines a list of gateways this HttpRoute is attached to, as one of the routing rules to route the requests served by the gateway. Each gateway reference should match the pattern: &#x60;projects/_*_/locations/global/gateways/&#x60; |  [optional] |
|**hostnames** | **List&lt;String&gt;** | Required. Hostnames define a set of hosts that should match against the HTTP host header to select a HttpRoute to process the request. Hostname is the fully qualified domain name of a network host, as defined by RFC 1123 with the exception that: - IPs are not allowed. - A hostname may be prefixed with a wildcard label (&#x60;*.&#x60;). The wildcard label must appear by itself as the first label. Hostname can be \&quot;precise\&quot; which is a domain name without the terminating dot of a network host (e.g. &#x60;foo.example.com&#x60;) or \&quot;wildcard\&quot;, which is a domain name prefixed with a single wildcard label (e.g. &#x60;*.example.com&#x60;). Note that as per RFC1035 and RFC1123, a label must consist of lower case alphanumeric characters or &#39;-&#39;, and must start and end with an alphanumeric character. No other punctuation is allowed. The routes associated with a Mesh or Gateways must have unique hostnames. If you attempt to attach multiple routes with conflicting hostnames, the configuration will be rejected. For example, while it is acceptable for routes for the hostnames &#x60;*.foo.bar.com&#x60; and &#x60;*.bar.com&#x60; to be associated with the same Mesh (or Gateways under the same scope), it is not possible to associate two routes both with &#x60;*.bar.com&#x60; or both with &#x60;bar.com&#x60;. |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | Optional. Set of label tags associated with the HttpRoute resource. |  [optional] |
|**meshes** | **List&lt;String&gt;** | Optional. Meshes defines a list of meshes this HttpRoute is attached to, as one of the routing rules to route the requests served by the mesh. Each mesh reference should match the pattern: &#x60;projects/_*_/locations/global/meshes/&#x60; The attached Mesh should be of a type SIDECAR |  [optional] |
|**name** | **String** | Required. Name of the HttpRoute resource. It matches pattern &#x60;projects/_*_/locations/global/httpRoutes/http_route_name&gt;&#x60;. |  [optional] |
|**rules** | [**List&lt;HttpRouteRouteRule&gt;**](HttpRouteRouteRule.md) | Required. Rules that define how traffic is routed and handled. Rules will be matched sequentially based on the RouteMatch specified for the rule. |  [optional] |
|**selfLink** | **String** | Output only. Server-defined URL of this resource |  [optional] [readonly] |
|**updateTime** | **String** | Output only. The timestamp when the resource was updated. |  [optional] [readonly] |



