

# EndpointPolicy

EndpointPolicy is a resource that helps apply desired configuration on the endpoints that match specific criteria. For example, this resource can be used to apply \"authentication config\" an all endpoints that serve on port 8080.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**authorizationPolicy** | **String** | Optional. This field specifies the URL of AuthorizationPolicy resource that applies authorization policies to the inbound traffic at the matched endpoints. Refer to Authorization. If this field is not specified, authorization is disabled(no authz checks) for this endpoint. |  [optional] |
|**clientTlsPolicy** | **String** | Optional. A URL referring to a ClientTlsPolicy resource. ClientTlsPolicy can be set to specify the authentication for traffic from the proxy to the actual endpoints. More specifically, it is applied to the outgoing traffic from the proxy to the endpoint. This is typically used for sidecar model where the proxy identifies itself as endpoint to the control plane, with the connection between sidecar and endpoint requiring authentication. If this field is not set, authentication is disabled(open). Applicable only when EndpointPolicyType is SIDECAR_PROXY. |  [optional] |
|**createTime** | **String** | Output only. The timestamp when the resource was created. |  [optional] [readonly] |
|**description** | **String** | Optional. A free-text description of the resource. Max length 1024 characters. |  [optional] |
|**endpointMatcher** | [**EndpointMatcher**](EndpointMatcher.md) |  |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | Optional. Set of label tags associated with the EndpointPolicy resource. |  [optional] |
|**name** | **String** | Required. Name of the EndpointPolicy resource. It matches pattern &#x60;projects/{project}/locations/global/endpointPolicies/{endpoint_policy}&#x60;. |  [optional] |
|**serverTlsPolicy** | **String** | Optional. A URL referring to ServerTlsPolicy resource. ServerTlsPolicy is used to determine the authentication policy to be applied to terminate the inbound traffic at the identified backends. If this field is not set, authentication is disabled(open) for this endpoint. |  [optional] |
|**trafficPortSelector** | [**TrafficPortSelector**](TrafficPortSelector.md) |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Required. The type of endpoint policy. This is primarily used to validate the configuration. |  [optional] |
|**updateTime** | **String** | Output only. The timestamp when the resource was updated. |  [optional] [readonly] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| ENDPOINT_POLICY_TYPE_UNSPECIFIED | &quot;ENDPOINT_POLICY_TYPE_UNSPECIFIED&quot; |
| SIDECAR_PROXY | &quot;SIDECAR_PROXY&quot; |
| GRPC_SERVER | &quot;GRPC_SERVER&quot; |



