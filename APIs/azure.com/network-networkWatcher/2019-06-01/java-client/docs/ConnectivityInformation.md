

# ConnectivityInformation

Information on the connectivity status.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**avgLatencyInMs** | **Integer** | Average latency in milliseconds. |  [optional] [readonly] |
|**connectionStatus** | [**ConnectionStatusEnum**](#ConnectionStatusEnum) | The connection status. |  [optional] [readonly] |
|**hops** | [**List&lt;ConnectivityHop&gt;**](ConnectivityHop.md) | List of hops between the source and the destination. |  [optional] [readonly] |
|**maxLatencyInMs** | **Integer** | Maximum latency in milliseconds. |  [optional] [readonly] |
|**minLatencyInMs** | **Integer** | Minimum latency in milliseconds. |  [optional] [readonly] |
|**probesFailed** | **Integer** | Number of failed probes. |  [optional] [readonly] |
|**probesSent** | **Integer** | Total number of probes sent. |  [optional] [readonly] |



## Enum: ConnectionStatusEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;Unknown&quot; |
| CONNECTED | &quot;Connected&quot; |
| DISCONNECTED | &quot;Disconnected&quot; |
| DEGRADED | &quot;Degraded&quot; |



