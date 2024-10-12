

# Gateway

Gateway represents the configuration for a proxy, typically a load balancer. It captures the ip:port over which the services are exposed by the proxy, along with any policy configurations. Routes have reference to to Gateways to dictate how requests should be routed by this Gateway. Next id: 32

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**addresses** | **List&lt;String&gt;** | Optional. Zero or one IPv4 or IPv6 address on which the Gateway will receive the traffic. When no address is provided, an IP from the subnetwork is allocated This field only applies to gateways of type &#39;SECURE_WEB_GATEWAY&#39;. Gateways of type &#39;OPEN_MESH&#39; listen on 0.0.0.0 for IPv4 and :: for IPv6. |  [optional] |
|**certificateUrls** | **List&lt;String&gt;** | Optional. A fully-qualified Certificates URL reference. The proxy presents a Certificate (selected based on SNI) when establishing a TLS connection. This feature only applies to gateways of type &#39;SECURE_WEB_GATEWAY&#39;. |  [optional] |
|**createTime** | **String** | Output only. The timestamp when the resource was created. |  [optional] [readonly] |
|**description** | **String** | Optional. A free-text description of the resource. Max length 1024 characters. |  [optional] |
|**envoyHeaders** | [**EnvoyHeadersEnum**](#EnvoyHeadersEnum) | Optional. Determines if envoy will insert internal debug headers into upstream requests. Other Envoy headers may still be injected. By default, envoy will not insert any debug headers. |  [optional] |
|**gatewaySecurityPolicy** | **String** | Optional. A fully-qualified GatewaySecurityPolicy URL reference. Defines how a server should apply security policy to inbound (VM to Proxy) initiated connections. For example: &#x60;projects/_*_/locations/_*_/gatewaySecurityPolicies/swg-policy&#x60;. This policy is specific to gateways of type &#39;SECURE_WEB_GATEWAY&#39;. |  [optional] |
|**ipVersion** | [**IpVersionEnum**](#IpVersionEnum) | Optional. The IP Version that will be used by this gateway. Valid options are IPV4 or IPV6. Default is IPV4. |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | Optional. Set of label tags associated with the Gateway resource. |  [optional] |
|**name** | **String** | Required. Name of the Gateway resource. It matches pattern &#x60;projects/_*_/locations/_*_/gateways/&#x60;. |  [optional] |
|**network** | **String** | Optional. The relative resource name identifying the VPC network that is using this configuration. For example: &#x60;projects/_*_/global/networks/network-1&#x60;. Currently, this field is specific to gateways of type &#39;SECURE_WEB_GATEWAY&#39;. |  [optional] |
|**ports** | **List&lt;Integer&gt;** | Required. One or more port numbers (1-65535), on which the Gateway will receive traffic. The proxy binds to the specified ports. Gateways of type &#39;SECURE_WEB_GATEWAY&#39; are limited to 1 port. Gateways of type &#39;OPEN_MESH&#39; listen on 0.0.0.0 for IPv4 and :: for IPv6 and support multiple ports. |  [optional] |
|**scope** | **String** | Optional. Scope determines how configuration across multiple Gateway instances are merged. The configuration for multiple Gateway instances with the same scope will be merged as presented as a single coniguration to the proxy/load balancer. Max length 64 characters. Scope should start with a letter and can only have letters, numbers, hyphens. |  [optional] |
|**selfLink** | **String** | Output only. Server-defined URL of this resource |  [optional] [readonly] |
|**serverTlsPolicy** | **String** | Optional. A fully-qualified ServerTLSPolicy URL reference. Specifies how TLS traffic is terminated. If empty, TLS termination is disabled. |  [optional] |
|**subnetwork** | **String** | Optional. The relative resource name identifying the subnetwork in which this SWG is allocated. For example: &#x60;projects/_*_/regions/us-central1/subnetworks/network-1&#x60; Currently, this field is specific to gateways of type &#39;SECURE_WEB_GATEWAY\&quot;. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Immutable. The type of the customer managed gateway. This field is required. If unspecified, an error is returned. |  [optional] |
|**updateTime** | **String** | Output only. The timestamp when the resource was updated. |  [optional] [readonly] |



## Enum: EnvoyHeadersEnum

| Name | Value |
|---- | -----|
| ENVOY_HEADERS_UNSPECIFIED | &quot;ENVOY_HEADERS_UNSPECIFIED&quot; |
| NONE | &quot;NONE&quot; |
| DEBUG_HEADERS | &quot;DEBUG_HEADERS&quot; |



## Enum: IpVersionEnum

| Name | Value |
|---- | -----|
| IP_VERSION_UNSPECIFIED | &quot;IP_VERSION_UNSPECIFIED&quot; |
| IPV4 | &quot;IPV4&quot; |
| IPV6 | &quot;IPV6&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| TYPE_UNSPECIFIED | &quot;TYPE_UNSPECIFIED&quot; |
| OPEN_MESH | &quot;OPEN_MESH&quot; |
| SECURE_WEB_GATEWAY | &quot;SECURE_WEB_GATEWAY&quot; |



