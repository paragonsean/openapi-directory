

# Mesh

Mesh represents a logical configuration grouping for workload to workload communication within a service mesh. Routes that point to mesh dictate how requests are routed within this logical mesh boundary.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | Output only. The timestamp when the resource was created. |  [optional] [readonly] |
|**description** | **String** | Optional. A free-text description of the resource. Max length 1024 characters. |  [optional] |
|**envoyHeaders** | [**EnvoyHeadersEnum**](#EnvoyHeadersEnum) | Optional. Determines if envoy will insert internal debug headers into upstream requests. Other Envoy headers may still be injected. By default, envoy will not insert any debug headers. |  [optional] |
|**interceptionPort** | **Integer** | Optional. If set to a valid TCP port (1-65535), instructs the SIDECAR proxy to listen on the specified port of localhost (127.0.0.1) address. The SIDECAR proxy will expect all traffic to be redirected to this port regardless of its actual ip:port destination. If unset, a port &#39;15001&#39; is used as the interception port. This is applicable only for sidecar proxy deployments. |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | Optional. Set of label tags associated with the Mesh resource. |  [optional] |
|**name** | **String** | Required. Name of the Mesh resource. It matches pattern &#x60;projects/_*_/locations/global/meshes/&#x60;. |  [optional] |
|**selfLink** | **String** | Output only. Server-defined URL of this resource |  [optional] [readonly] |
|**updateTime** | **String** | Output only. The timestamp when the resource was updated. |  [optional] [readonly] |



## Enum: EnvoyHeadersEnum

| Name | Value |
|---- | -----|
| ENVOY_HEADERS_UNSPECIFIED | &quot;ENVOY_HEADERS_UNSPECIFIED&quot; |
| NONE | &quot;NONE&quot; |
| DEBUG_HEADERS | &quot;DEBUG_HEADERS&quot; |



