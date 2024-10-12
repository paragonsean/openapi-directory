

# ConsumerPscConnection

PSC connection details on consumer side.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**error** | [**GoogleRpcStatus**](GoogleRpcStatus.md) |  |  [optional] |
|**errorInfo** | [**GoogleRpcErrorInfo**](GoogleRpcErrorInfo.md) |  |  [optional] |
|**errorType** | [**ErrorTypeEnum**](#ErrorTypeEnum) | The error type indicates whether the error is consumer facing, producer facing or system internal. |  [optional] |
|**forwardingRule** | **String** | The URI of the consumer forwarding rule created. Example: projects/{projectNumOrId}/regions/us-east1/networks/{resourceId}. |  [optional] |
|**gceOperation** | **String** | The last Compute Engine operation to setup PSC connection. |  [optional] |
|**ip** | **String** | The IP literal allocated on the consumer network for the PSC forwarding rule that is created to connect to the producer service attachment in this service connection map. |  [optional] |
|**network** | **String** | The consumer network whose PSC forwarding rule is connected to the service attachments in this service connection map. Note that the network could be on a different project (shared VPC). |  [optional] |
|**project** | **String** | The consumer project whose PSC forwarding rule is connected to the service attachments in this service connection map. |  [optional] |
|**pscConnectionId** | **String** | The PSC connection id of the PSC forwarding rule connected to the service attachments in this service connection map. |  [optional] |
|**selectedSubnetwork** | **String** | Output only. The URI of the selected subnetwork selected to allocate IP address for this connection. |  [optional] [readonly] |
|**serviceAttachmentUri** | **String** | The URI of a service attachment which is the target of the PSC connection. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | The state of the PSC connection. |  [optional] |



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



