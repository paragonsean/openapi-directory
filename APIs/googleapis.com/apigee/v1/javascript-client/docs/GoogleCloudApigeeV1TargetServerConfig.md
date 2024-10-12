# ApigeeApi.GoogleCloudApigeeV1TargetServerConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **Boolean** | Whether the target server is enabled. An empty/omitted value for this field should be interpreted as true. | [optional] 
**host** | **String** | Host name of the target server. | [optional] 
**name** | **String** | Target server revision name in the following format: &#x60;organizations/{org}/environments/{env}/targetservers/{targetserver}/revisions/{rev}&#x60; | [optional] 
**port** | **Number** | Port number for the target server. | [optional] 
**protocol** | **String** | The protocol used by this target server. | [optional] 
**tlsInfo** | [**GoogleCloudApigeeV1TlsInfoConfig**](GoogleCloudApigeeV1TlsInfoConfig.md) |  | [optional] 



## Enum: ProtocolEnum


* `PROTOCOL_UNSPECIFIED` (value: `"PROTOCOL_UNSPECIFIED"`)

* `HTTP` (value: `"HTTP"`)

* `HTTP2` (value: `"HTTP2"`)

* `GRPC_TARGET` (value: `"GRPC_TARGET"`)

* `GRPC` (value: `"GRPC"`)

* `EXTERNAL_CALLOUT` (value: `"EXTERNAL_CALLOUT"`)




