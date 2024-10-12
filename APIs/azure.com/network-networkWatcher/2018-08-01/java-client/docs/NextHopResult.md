

# NextHopResult

The information about next hop from the specified VM.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nextHopIpAddress** | **String** | Next hop IP Address |  [optional] |
|**nextHopType** | [**NextHopTypeEnum**](#NextHopTypeEnum) | Next hop type. |  [optional] |
|**routeTableId** | **String** | The resource identifier for the route table associated with the route being returned. If the route being returned does not correspond to any user created routes then this field will be the string &#39;System Route&#39;. |  [optional] |



## Enum: NextHopTypeEnum

| Name | Value |
|---- | -----|
| INTERNET | &quot;Internet&quot; |
| VIRTUAL_APPLIANCE | &quot;VirtualAppliance&quot; |
| VIRTUAL_NETWORK_GATEWAY | &quot;VirtualNetworkGateway&quot; |
| VNET_LOCAL | &quot;VnetLocal&quot; |
| HYPER_NET_GATEWAY | &quot;HyperNetGateway&quot; |
| NONE | &quot;None&quot; |



