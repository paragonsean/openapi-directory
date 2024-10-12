

# GoogleCloudApigeeV1TargetServerConfig


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**enabled** | **Boolean** | Whether the target server is enabled. An empty/omitted value for this field should be interpreted as true. |  [optional] |
|**host** | **String** | Host name of the target server. |  [optional] |
|**name** | **String** | Target server revision name in the following format: &#x60;organizations/{org}/environments/{env}/targetservers/{targetserver}/revisions/{rev}&#x60; |  [optional] |
|**port** | **Integer** | Port number for the target server. |  [optional] |
|**protocol** | [**ProtocolEnum**](#ProtocolEnum) | The protocol used by this target server. |  [optional] |
|**tlsInfo** | [**GoogleCloudApigeeV1TlsInfoConfig**](GoogleCloudApigeeV1TlsInfoConfig.md) |  |  [optional] |



## Enum: ProtocolEnum

| Name | Value |
|---- | -----|
| PROTOCOL_UNSPECIFIED | &quot;PROTOCOL_UNSPECIFIED&quot; |
| HTTP | &quot;HTTP&quot; |
| HTTP2 | &quot;HTTP2&quot; |
| GRPC_TARGET | &quot;GRPC_TARGET&quot; |
| GRPC | &quot;GRPC&quot; |
| EXTERNAL_CALLOUT | &quot;EXTERNAL_CALLOUT&quot; |



