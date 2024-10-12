

# GetNetworkApplianceTrafficShapingUplinkSelection200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**activeActiveAutoVpnEnabled** | **Boolean** | Whether active-active AutoVPN is enabled |  [optional] |
|**defaultUplink** | [**DefaultUplinkEnum**](#DefaultUplinkEnum) | The default uplink. Must be one of: &#39;wan1&#39; or &#39;wan2&#39; |  [optional] |
|**failoverAndFailback** | [**GetNetworkApplianceTrafficShapingUplinkSelection200ResponseFailoverAndFailback**](GetNetworkApplianceTrafficShapingUplinkSelection200ResponseFailoverAndFailback.md) |  |  [optional] |
|**loadBalancingEnabled** | **Boolean** | Whether load balancing is enabled |  [optional] |
|**vpnTrafficUplinkPreferences** | [**List&lt;GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInner&gt;**](GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInner.md) | Uplink preference rules for VPN traffic |  [optional] |
|**wanTrafficUplinkPreferences** | [**List&lt;GetNetworkApplianceTrafficShapingUplinkSelection200ResponseWanTrafficUplinkPreferencesInner&gt;**](GetNetworkApplianceTrafficShapingUplinkSelection200ResponseWanTrafficUplinkPreferencesInner.md) | Uplink preference rules for WAN traffic |  [optional] |



## Enum: DefaultUplinkEnum

| Name | Value |
|---- | -----|
| WAN1 | &quot;wan1&quot; |
| WAN2 | &quot;wan2&quot; |



