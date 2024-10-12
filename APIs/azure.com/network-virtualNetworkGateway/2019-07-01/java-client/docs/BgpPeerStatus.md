

# BgpPeerStatus

BGP peer status details.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**asn** | **Integer** | The autonomous system number of the remote BGP peer. |  [optional] [readonly] |
|**connectedDuration** | **String** | For how long the peering has been up. |  [optional] [readonly] |
|**localAddress** | **String** | The virtual network gateway&#39;s local address. |  [optional] [readonly] |
|**messagesReceived** | **Long** | The number of BGP messages received. |  [optional] [readonly] |
|**messagesSent** | **Long** | The number of BGP messages sent. |  [optional] [readonly] |
|**neighbor** | **String** | The remote BGP peer. |  [optional] [readonly] |
|**routesReceived** | **Long** | The number of routes learned from this peer. |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | The BGP peer state. |  [optional] [readonly] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;Unknown&quot; |
| STOPPED | &quot;Stopped&quot; |
| IDLE | &quot;Idle&quot; |
| CONNECTING | &quot;Connecting&quot; |
| CONNECTED | &quot;Connected&quot; |



