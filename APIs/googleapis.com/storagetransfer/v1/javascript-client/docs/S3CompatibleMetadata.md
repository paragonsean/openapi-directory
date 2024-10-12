# StorageTransferApi.S3CompatibleMetadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authMethod** | **String** | Specifies the authentication and authorization method used by the storage service. When not specified, Transfer Service will attempt to determine right auth method to use. | [optional] 
**listApi** | **String** | The Listing API to use for discovering objects. When not specified, Transfer Service will attempt to determine the right API to use. | [optional] 
**protocol** | **String** | Specifies the network protocol of the agent. When not specified, the default value of NetworkProtocol NETWORK_PROTOCOL_HTTPS is used. | [optional] 
**requestModel** | **String** | Specifies the API request model used to call the storage service. When not specified, the default value of RequestModel REQUEST_MODEL_VIRTUAL_HOSTED_STYLE is used. | [optional] 



## Enum: AuthMethodEnum


* `UNSPECIFIED` (value: `"AUTH_METHOD_UNSPECIFIED"`)

* `AWS_SIGNATURE_V4` (value: `"AUTH_METHOD_AWS_SIGNATURE_V4"`)

* `AWS_SIGNATURE_V2` (value: `"AUTH_METHOD_AWS_SIGNATURE_V2"`)





## Enum: ListApiEnum


* `API_UNSPECIFIED` (value: `"LIST_API_UNSPECIFIED"`)

* `OBJECTS_V2` (value: `"LIST_OBJECTS_V2"`)

* `OBJECTS` (value: `"LIST_OBJECTS"`)





## Enum: ProtocolEnum


* `UNSPECIFIED` (value: `"NETWORK_PROTOCOL_UNSPECIFIED"`)

* `HTTPS` (value: `"NETWORK_PROTOCOL_HTTPS"`)

* `HTTP` (value: `"NETWORK_PROTOCOL_HTTP"`)





## Enum: RequestModelEnum


* `UNSPECIFIED` (value: `"REQUEST_MODEL_UNSPECIFIED"`)

* `VIRTUAL_HOSTED_STYLE` (value: `"REQUEST_MODEL_VIRTUAL_HOSTED_STYLE"`)

* `PATH_STYLE` (value: `"REQUEST_MODEL_PATH_STYLE"`)




