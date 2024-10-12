

# EffectiveRoute

Effective Route

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**addressPrefix** | **List&lt;String&gt;** | Gets address prefixes of the effective routes in CIDR notation. |  [optional] |
|**name** | **String** | Gets the name of the user defined route. This is optional. |  [optional] |
|**nextHopIpAddress** | **List&lt;String&gt;** | Gets the IP address of the next hop of the effective route |  [optional] |
|**nextHopType** | [**NextHopTypeEnum**](#NextHopTypeEnum) | Gets or sets the type of Azure hop the packet should be sent to. |  [optional] |
|**source** | [**SourceEnum**](#SourceEnum) | Gets who created the route |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Gets value of effective route |  [optional] |



## Enum: NextHopTypeEnum

| Name | Value |
|---- | -----|
| VIRTUAL_NETWORK_GATEWAY | &quot;VirtualNetworkGateway&quot; |
| VNET_LOCAL | &quot;VnetLocal&quot; |
| INTERNET | &quot;Internet&quot; |
| VIRTUAL_APPLIANCE | &quot;VirtualAppliance&quot; |
| NONE | &quot;None&quot; |



## Enum: SourceEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;Unknown&quot; |
| USER | &quot;User&quot; |
| VIRTUAL_NETWORK_GATEWAY | &quot;VirtualNetworkGateway&quot; |
| DEFAULT | &quot;Default&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;Active&quot; |
| INVALID | &quot;Invalid&quot; |



