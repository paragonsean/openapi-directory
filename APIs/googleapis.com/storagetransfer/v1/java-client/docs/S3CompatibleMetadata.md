

# S3CompatibleMetadata

S3CompatibleMetadata contains the metadata fields that apply to the basic types of S3-compatible data providers.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**authMethod** | [**AuthMethodEnum**](#AuthMethodEnum) | Specifies the authentication and authorization method used by the storage service. When not specified, Transfer Service will attempt to determine right auth method to use. |  [optional] |
|**listApi** | [**ListApiEnum**](#ListApiEnum) | The Listing API to use for discovering objects. When not specified, Transfer Service will attempt to determine the right API to use. |  [optional] |
|**protocol** | [**ProtocolEnum**](#ProtocolEnum) | Specifies the network protocol of the agent. When not specified, the default value of NetworkProtocol NETWORK_PROTOCOL_HTTPS is used. |  [optional] |
|**requestModel** | [**RequestModelEnum**](#RequestModelEnum) | Specifies the API request model used to call the storage service. When not specified, the default value of RequestModel REQUEST_MODEL_VIRTUAL_HOSTED_STYLE is used. |  [optional] |



## Enum: AuthMethodEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;AUTH_METHOD_UNSPECIFIED&quot; |
| AWS_SIGNATURE_V4 | &quot;AUTH_METHOD_AWS_SIGNATURE_V4&quot; |
| AWS_SIGNATURE_V2 | &quot;AUTH_METHOD_AWS_SIGNATURE_V2&quot; |



## Enum: ListApiEnum

| Name | Value |
|---- | -----|
| API_UNSPECIFIED | &quot;LIST_API_UNSPECIFIED&quot; |
| OBJECTS_V2 | &quot;LIST_OBJECTS_V2&quot; |
| OBJECTS | &quot;LIST_OBJECTS&quot; |



## Enum: ProtocolEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;NETWORK_PROTOCOL_UNSPECIFIED&quot; |
| HTTPS | &quot;NETWORK_PROTOCOL_HTTPS&quot; |
| HTTP | &quot;NETWORK_PROTOCOL_HTTP&quot; |



## Enum: RequestModelEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;REQUEST_MODEL_UNSPECIFIED&quot; |
| VIRTUAL_HOSTED_STYLE | &quot;REQUEST_MODEL_VIRTUAL_HOSTED_STYLE&quot; |
| PATH_STYLE | &quot;REQUEST_MODEL_PATH_STYLE&quot; |



