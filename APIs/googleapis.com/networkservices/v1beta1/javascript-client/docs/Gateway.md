# NetworkServicesApi.Gateway

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addresses** | **[String]** | Optional. Zero or one IPv4 or IPv6 address on which the Gateway will receive the traffic. When no address is provided, an IP from the subnetwork is allocated This field only applies to gateways of type &#39;SECURE_WEB_GATEWAY&#39;. Gateways of type &#39;OPEN_MESH&#39; listen on 0.0.0.0 for IPv4 and :: for IPv6. | [optional] 
**certificateUrls** | **[String]** | Optional. A fully-qualified Certificates URL reference. The proxy presents a Certificate (selected based on SNI) when establishing a TLS connection. This feature only applies to gateways of type &#39;SECURE_WEB_GATEWAY&#39;. | [optional] 
**createTime** | **String** | Output only. The timestamp when the resource was created. | [optional] [readonly] 
**description** | **String** | Optional. A free-text description of the resource. Max length 1024 characters. | [optional] 
**envoyHeaders** | **String** | Optional. Determines if envoy will insert internal debug headers into upstream requests. Other Envoy headers may still be injected. By default, envoy will not insert any debug headers. | [optional] 
**gatewaySecurityPolicy** | **String** | Optional. A fully-qualified GatewaySecurityPolicy URL reference. Defines how a server should apply security policy to inbound (VM to Proxy) initiated connections. For example: &#x60;projects/_*_/locations/_*_/gatewaySecurityPolicies/swg-policy&#x60;. This policy is specific to gateways of type &#39;SECURE_WEB_GATEWAY&#39;. | [optional] 
**ipVersion** | **String** | Optional. The IP Version that will be used by this gateway. Valid options are IPV4 or IPV6. Default is IPV4. | [optional] 
**labels** | **{String: String}** | Optional. Set of label tags associated with the Gateway resource. | [optional] 
**name** | **String** | Required. Name of the Gateway resource. It matches pattern &#x60;projects/_*_/locations/_*_/gateways/&#x60;. | [optional] 
**network** | **String** | Optional. The relative resource name identifying the VPC network that is using this configuration. For example: &#x60;projects/_*_/global/networks/network-1&#x60;. Currently, this field is specific to gateways of type &#39;SECURE_WEB_GATEWAY&#39;. | [optional] 
**ports** | **[Number]** | Required. One or more port numbers (1-65535), on which the Gateway will receive traffic. The proxy binds to the specified ports. Gateways of type &#39;SECURE_WEB_GATEWAY&#39; are limited to 1 port. Gateways of type &#39;OPEN_MESH&#39; listen on 0.0.0.0 for IPv4 and :: for IPv6 and support multiple ports. | [optional] 
**scope** | **String** | Optional. Scope determines how configuration across multiple Gateway instances are merged. The configuration for multiple Gateway instances with the same scope will be merged as presented as a single coniguration to the proxy/load balancer. Max length 64 characters. Scope should start with a letter and can only have letters, numbers, hyphens. | [optional] 
**selfLink** | **String** | Output only. Server-defined URL of this resource | [optional] [readonly] 
**serverTlsPolicy** | **String** | Optional. A fully-qualified ServerTLSPolicy URL reference. Specifies how TLS traffic is terminated. If empty, TLS termination is disabled. | [optional] 
**subnetwork** | **String** | Optional. The relative resource name identifying the subnetwork in which this SWG is allocated. For example: &#x60;projects/_*_/regions/us-central1/subnetworks/network-1&#x60; Currently, this field is specific to gateways of type &#39;SECURE_WEB_GATEWAY\&quot;. | [optional] 
**type** | **String** | Immutable. The type of the customer managed gateway. This field is required. If unspecified, an error is returned. | [optional] 
**updateTime** | **String** | Output only. The timestamp when the resource was updated. | [optional] [readonly] 



## Enum: EnvoyHeadersEnum


* `ENVOY_HEADERS_UNSPECIFIED` (value: `"ENVOY_HEADERS_UNSPECIFIED"`)

* `NONE` (value: `"NONE"`)

* `DEBUG_HEADERS` (value: `"DEBUG_HEADERS"`)





## Enum: IpVersionEnum


* `IP_VERSION_UNSPECIFIED` (value: `"IP_VERSION_UNSPECIFIED"`)

* `IPV4` (value: `"IPV4"`)

* `IPV6` (value: `"IPV6"`)





## Enum: TypeEnum


* `TYPE_UNSPECIFIED` (value: `"TYPE_UNSPECIFIED"`)

* `OPEN_MESH` (value: `"OPEN_MESH"`)

* `SECURE_WEB_GATEWAY` (value: `"SECURE_WEB_GATEWAY"`)




