# MerakiDashboardApi.GetNetworkApplianceTrafficShapingUplinkSelection200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activeActiveAutoVpnEnabled** | **Boolean** | Whether active-active AutoVPN is enabled | [optional] 
**defaultUplink** | **String** | The default uplink. Must be one of: &#39;wan1&#39; or &#39;wan2&#39; | [optional] 
**failoverAndFailback** | [**GetNetworkApplianceTrafficShapingUplinkSelection200ResponseFailoverAndFailback**](GetNetworkApplianceTrafficShapingUplinkSelection200ResponseFailoverAndFailback.md) |  | [optional] 
**loadBalancingEnabled** | **Boolean** | Whether load balancing is enabled | [optional] 
**vpnTrafficUplinkPreferences** | [**[GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInner]**](GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInner.md) | Uplink preference rules for VPN traffic | [optional] 
**wanTrafficUplinkPreferences** | [**[GetNetworkApplianceTrafficShapingUplinkSelection200ResponseWanTrafficUplinkPreferencesInner]**](GetNetworkApplianceTrafficShapingUplinkSelection200ResponseWanTrafficUplinkPreferencesInner.md) | Uplink preference rules for WAN traffic | [optional] 



## Enum: DefaultUplinkEnum


* `wan1` (value: `"wan1"`)

* `wan2` (value: `"wan2"`)




