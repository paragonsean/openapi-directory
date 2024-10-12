# NetworkServicesApi.Mesh

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | Output only. The timestamp when the resource was created. | [optional] [readonly] 
**description** | **String** | Optional. A free-text description of the resource. Max length 1024 characters. | [optional] 
**envoyHeaders** | **String** | Optional. Determines if envoy will insert internal debug headers into upstream requests. Other Envoy headers may still be injected. By default, envoy will not insert any debug headers. | [optional] 
**interceptionPort** | **Number** | Optional. If set to a valid TCP port (1-65535), instructs the SIDECAR proxy to listen on the specified port of localhost (127.0.0.1) address. The SIDECAR proxy will expect all traffic to be redirected to this port regardless of its actual ip:port destination. If unset, a port &#39;15001&#39; is used as the interception port. This is applicable only for sidecar proxy deployments. | [optional] 
**labels** | **{String: String}** | Optional. Set of label tags associated with the Mesh resource. | [optional] 
**name** | **String** | Required. Name of the Mesh resource. It matches pattern &#x60;projects/_*_/locations/global/meshes/&#x60;. | [optional] 
**selfLink** | **String** | Output only. Server-defined URL of this resource | [optional] [readonly] 
**updateTime** | **String** | Output only. The timestamp when the resource was updated. | [optional] [readonly] 



## Enum: EnvoyHeadersEnum


* `ENVOY_HEADERS_UNSPECIFIED` (value: `"ENVOY_HEADERS_UNSPECIFIED"`)

* `NONE` (value: `"NONE"`)

* `DEBUG_HEADERS` (value: `"DEBUG_HEADERS"`)




