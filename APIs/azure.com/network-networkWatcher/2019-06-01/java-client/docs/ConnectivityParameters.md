

# ConnectivityParameters

Parameters that determine how the connectivity check will be performed.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**destination** | [**ConnectivityDestination**](ConnectivityDestination.md) |  |  |
|**protocol** | [**ProtocolEnum**](#ProtocolEnum) | Network protocol. |  [optional] |
|**protocolConfiguration** | [**ProtocolConfiguration**](ProtocolConfiguration.md) |  |  [optional] |
|**source** | [**ConnectivitySource**](ConnectivitySource.md) |  |  |



## Enum: ProtocolEnum

| Name | Value |
|---- | -----|
| TCP | &quot;Tcp&quot; |
| HTTP | &quot;Http&quot; |
| HTTPS | &quot;Https&quot; |
| ICMP | &quot;Icmp&quot; |



