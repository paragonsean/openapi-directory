# NetworkManagementClient.ConnectivityInformation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avgLatencyInMs** | **Number** | Average latency in milliseconds. | [optional] [readonly] 
**connectionStatus** | **String** | The connection status. | [optional] [readonly] 
**hops** | [**[ConnectivityHop]**](ConnectivityHop.md) | List of hops between the source and the destination. | [optional] [readonly] 
**maxLatencyInMs** | **Number** | Maximum latency in milliseconds. | [optional] [readonly] 
**minLatencyInMs** | **Number** | Minimum latency in milliseconds. | [optional] [readonly] 
**probesFailed** | **Number** | Number of failed probes. | [optional] [readonly] 
**probesSent** | **Number** | Total number of probes sent. | [optional] [readonly] 



## Enum: ConnectionStatusEnum


* `Unknown` (value: `"Unknown"`)

* `Connected` (value: `"Connected"`)

* `Disconnected` (value: `"Disconnected"`)

* `Degraded` (value: `"Degraded"`)




