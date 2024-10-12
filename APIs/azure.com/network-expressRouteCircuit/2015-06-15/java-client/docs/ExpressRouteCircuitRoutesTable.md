

# ExpressRouteCircuitRoutesTable

The routes table associated with the ExpressRouteCircuit

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**addressPrefix** | **String** | Gets AddressPrefix. |  [optional] |
|**asPath** | **String** | Gets AsPath. |  [optional] |
|**nextHopIP** | **String** | Gets NextHopIP. |  [optional] |
|**nextHopType** | [**NextHopTypeEnum**](#NextHopTypeEnum) | Gets NextHopType. |  |



## Enum: NextHopTypeEnum

| Name | Value |
|---- | -----|
| VIRTUAL_NETWORK_GATEWAY | &quot;VirtualNetworkGateway&quot; |
| VNET_LOCAL | &quot;VnetLocal&quot; |
| INTERNET | &quot;Internet&quot; |
| VIRTUAL_APPLIANCE | &quot;VirtualAppliance&quot; |
| NONE | &quot;None&quot; |



