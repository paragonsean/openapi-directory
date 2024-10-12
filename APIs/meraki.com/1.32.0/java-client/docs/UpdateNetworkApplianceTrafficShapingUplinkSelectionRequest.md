

# UpdateNetworkApplianceTrafficShapingUplinkSelectionRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**activeActiveAutoVpnEnabled** | **Boolean** | Toggle for enabling or disabling active-active AutoVPN |  [optional] |
|**defaultUplink** | [**DefaultUplinkEnum**](#DefaultUplinkEnum) | The default uplink. Must be one of: &#39;wan1&#39; or &#39;wan2&#39; |  [optional] |
|**failoverAndFailback** | [**UpdateNetworkApplianceTrafficShapingUplinkSelectionRequestFailoverAndFailback**](UpdateNetworkApplianceTrafficShapingUplinkSelectionRequestFailoverAndFailback.md) |  |  [optional] |
|**loadBalancingEnabled** | **Boolean** | Toggle for enabling or disabling load balancing |  [optional] |
|**vpnTrafficUplinkPreferences** | [**List&lt;UpdateNetworkApplianceTrafficShapingUplinkSelectionRequestVpnTrafficUplinkPreferencesInner&gt;**](UpdateNetworkApplianceTrafficShapingUplinkSelectionRequestVpnTrafficUplinkPreferencesInner.md) | Array of uplink preference rules for VPN traffic |  [optional] |
|**wanTrafficUplinkPreferences** | [**List&lt;UpdateNetworkApplianceTrafficShapingUplinkSelectionRequestWanTrafficUplinkPreferencesInner&gt;**](UpdateNetworkApplianceTrafficShapingUplinkSelectionRequestWanTrafficUplinkPreferencesInner.md) | Array of uplink preference rules for WAN traffic |  [optional] |



## Enum: DefaultUplinkEnum

| Name | Value |
|---- | -----|
| WAN1 | &quot;wan1&quot; |
| WAN2 | &quot;wan2&quot; |



