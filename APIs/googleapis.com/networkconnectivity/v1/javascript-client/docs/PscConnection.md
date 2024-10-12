# NetworkConnectivityApi.PscConnection

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consumerAddress** | **String** | The resource reference of the consumer address. | [optional] 
**consumerForwardingRule** | **String** | The resource reference of the PSC Forwarding Rule within the consumer VPC. | [optional] 
**consumerTargetProject** | **String** | The project where the PSC connection is created. | [optional] 
**error** | [**GoogleRpcStatus**](GoogleRpcStatus.md) |  | [optional] 
**errorInfo** | [**GoogleRpcErrorInfo**](GoogleRpcErrorInfo.md) |  | [optional] 
**errorType** | **String** | The error type indicates whether the error is consumer facing, producer facing or system internal. | [optional] 
**gceOperation** | **String** | The last Compute Engine operation to setup PSC connection. | [optional] 
**pscConnectionId** | **String** | The PSC connection id of the PSC forwarding rule. | [optional] 
**selectedSubnetwork** | **String** | Output only. The URI of the subnetwork selected to allocate IP address for this connection. | [optional] [readonly] 
**state** | **String** | State of the PSC Connection | [optional] 



## Enum: ErrorTypeEnum


* `CONNECTION_ERROR_TYPE_UNSPECIFIED` (value: `"CONNECTION_ERROR_TYPE_UNSPECIFIED"`)

* `ERROR_INTERNAL` (value: `"ERROR_INTERNAL"`)

* `ERROR_CONSUMER_SIDE` (value: `"ERROR_CONSUMER_SIDE"`)

* `ERROR_PRODUCER_SIDE` (value: `"ERROR_PRODUCER_SIDE"`)





## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `ACTIVE` (value: `"ACTIVE"`)

* `FAILED` (value: `"FAILED"`)

* `CREATING` (value: `"CREATING"`)

* `DELETING` (value: `"DELETING"`)




