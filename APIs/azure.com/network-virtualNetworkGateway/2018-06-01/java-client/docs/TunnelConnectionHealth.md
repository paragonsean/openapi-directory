

# TunnelConnectionHealth

VirtualNetworkGatewayConnection properties

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**connectionStatus** | [**ConnectionStatusEnum**](#ConnectionStatusEnum) | Virtual network Gateway connection status |  [optional] [readonly] |
|**egressBytesTransferred** | **Long** | The Egress Bytes Transferred in this connection |  [optional] [readonly] |
|**ingressBytesTransferred** | **Long** | The Ingress Bytes Transferred in this connection |  [optional] [readonly] |
|**lastConnectionEstablishedUtcTime** | **String** | The time at which connection was established in Utc format. |  [optional] [readonly] |
|**tunnel** | **String** | Tunnel name. |  [optional] [readonly] |



## Enum: ConnectionStatusEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;Unknown&quot; |
| CONNECTING | &quot;Connecting&quot; |
| CONNECTED | &quot;Connected&quot; |
| NOT_CONNECTED | &quot;NotConnected&quot; |



