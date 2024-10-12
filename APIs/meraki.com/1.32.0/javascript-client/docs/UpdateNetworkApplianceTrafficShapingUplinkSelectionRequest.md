# MerakiDashboardApi.UpdateNetworkApplianceTrafficShapingUplinkSelectionRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activeActiveAutoVpnEnabled** | **Boolean** | Toggle for enabling or disabling active-active AutoVPN | [optional] 
**defaultUplink** | **String** | The default uplink. Must be one of: &#39;wan1&#39; or &#39;wan2&#39; | [optional] 
**failoverAndFailback** | [**UpdateNetworkApplianceTrafficShapingUplinkSelectionRequestFailoverAndFailback**](UpdateNetworkApplianceTrafficShapingUplinkSelectionRequestFailoverAndFailback.md) |  | [optional] 
**loadBalancingEnabled** | **Boolean** | Toggle for enabling or disabling load balancing | [optional] 
**vpnTrafficUplinkPreferences** | [**[UpdateNetworkApplianceTrafficShapingUplinkSelectionRequestVpnTrafficUplinkPreferencesInner]**](UpdateNetworkApplianceTrafficShapingUplinkSelectionRequestVpnTrafficUplinkPreferencesInner.md) | Array of uplink preference rules for VPN traffic | [optional] 
**wanTrafficUplinkPreferences** | [**[UpdateNetworkApplianceTrafficShapingUplinkSelectionRequestWanTrafficUplinkPreferencesInner]**](UpdateNetworkApplianceTrafficShapingUplinkSelectionRequestWanTrafficUplinkPreferencesInner.md) | Array of uplink preference rules for WAN traffic | [optional] 



## Enum: DefaultUplinkEnum


* `wan1` (value: `"wan1"`)

* `wan2` (value: `"wan2"`)




