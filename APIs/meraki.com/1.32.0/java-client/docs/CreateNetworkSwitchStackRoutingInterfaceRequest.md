

# CreateNetworkSwitchStackRoutingInterfaceRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**defaultGateway** | **String** | The next hop for any traffic that isn&#39;t going to a directly connected subnet or over a static route. This IP address must exist in a subnet with a routed interface. |  [optional] |
|**interfaceIp** | **String** | The IP address this switch stack will use for layer 3 routing on this VLAN or subnet. This cannot be the same as the switch&#39;s management IP. |  [optional] |
|**ipv6** | [**CreateNetworkSwitchStackRoutingInterfaceRequestIpv6**](CreateNetworkSwitchStackRoutingInterfaceRequestIpv6.md) |  |  [optional] |
|**multicastRouting** | [**MulticastRoutingEnum**](#MulticastRoutingEnum) | Enable multicast support if, multicast routing between VLANs is required. Options are, &#39;disabled&#39;, &#39;enabled&#39; or &#39;IGMP snooping querier&#39;. Default is &#39;disabled&#39;. |  [optional] |
|**name** | **String** | A friendly name or description for the interface or VLAN. |  |
|**ospfSettings** | [**CreateNetworkSwitchStackRoutingInterfaceRequestOspfSettings**](CreateNetworkSwitchStackRoutingInterfaceRequestOspfSettings.md) |  |  [optional] |
|**subnet** | **String** | The network that this routed interface is on, in CIDR notation (ex. 10.1.1.0/24). |  [optional] |
|**vlanId** | **Integer** | The VLAN this routed interface is on. VLAN must be between 1 and 4094. |  |



## Enum: MulticastRoutingEnum

| Name | Value |
|---- | -----|
| IGMP_SNOOPING_QUERIER | &quot;IGMP snooping querier&quot; |
| DISABLED | &quot;disabled&quot; |
| ENABLED | &quot;enabled&quot; |



