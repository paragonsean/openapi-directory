

# PscConnection

Information about a specific Private Service Connect connection.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**consumerAddress** | **String** | The resource reference of the consumer address. |  [optional] |
|**consumerForwardingRule** | **String** | The resource reference of the PSC Forwarding Rule within the consumer VPC. |  [optional] |
|**consumerTargetProject** | **String** | The project where the PSC connection is created. |  [optional] |
|**error** | [**GoogleRpcStatus**](GoogleRpcStatus.md) |  |  [optional] |
|**errorInfo** | [**GoogleRpcErrorInfo**](GoogleRpcErrorInfo.md) |  |  [optional] |
|**errorType** | [**ErrorTypeEnum**](#ErrorTypeEnum) | The error type indicates whether the error is consumer facing, producer facing or system internal. |  [optional] |
|**gceOperation** | **String** | The last Compute Engine operation to setup PSC connection. |  [optional] |
|**pscConnectionId** | **String** | The PSC connection id of the PSC forwarding rule. |  [optional] |
|**selectedSubnetwork** | **String** | Output only. The URI of the subnetwork selected to allocate IP address for this connection. |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | State of the PSC Connection |  [optional] |



## Enum: ErrorTypeEnum

| Name | Value |
|---- | -----|
| CONNECTION_ERROR_TYPE_UNSPECIFIED | &quot;CONNECTION_ERROR_TYPE_UNSPECIFIED&quot; |
| ERROR_INTERNAL | &quot;ERROR_INTERNAL&quot; |
| ERROR_CONSUMER_SIDE | &quot;ERROR_CONSUMER_SIDE&quot; |
| ERROR_PRODUCER_SIDE | &quot;ERROR_PRODUCER_SIDE&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| ACTIVE | &quot;ACTIVE&quot; |
| FAILED | &quot;FAILED&quot; |
| CREATING | &quot;CREATING&quot; |
| DELETING | &quot;DELETING&quot; |



