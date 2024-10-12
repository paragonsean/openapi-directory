# ApigeeApi.GoogleCloudApigeeV1TargetServer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **String** | Optional. A human-readable description of this TargetServer. | [optional] 
**host** | **String** | Required. The host name this target connects to. Value must be a valid hostname as described by RFC-1123. | [optional] 
**isEnabled** | **Boolean** | Optional. Enabling/disabling a TargetServer is useful when TargetServers are used in load balancing configurations, and one or more TargetServers need to taken out of rotation periodically. Defaults to true. | [optional] 
**name** | **String** | Required. The resource id of this target server. Values must match the regular expression  | [optional] 
**port** | **Number** | Required. The port number this target connects to on the given host. Value must be between 1 and 65535, inclusive. | [optional] 
**protocol** | **String** | Immutable. The protocol used by this TargetServer. | [optional] 
**sSLInfo** | [**GoogleCloudApigeeV1TlsInfo**](GoogleCloudApigeeV1TlsInfo.md) |  | [optional] 



## Enum: ProtocolEnum


* `PROTOCOL_UNSPECIFIED` (value: `"PROTOCOL_UNSPECIFIED"`)

* `HTTP` (value: `"HTTP"`)

* `HTTP2` (value: `"HTTP2"`)

* `GRPC_TARGET` (value: `"GRPC_TARGET"`)

* `GRPC` (value: `"GRPC"`)

* `EXTERNAL_CALLOUT` (value: `"EXTERNAL_CALLOUT"`)




