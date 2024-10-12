# MerakiDashboardApi.UpdateNetworkApplianceFirewallOneToManyNatRulesRequestRulesInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**portRules** | [**[UpdateNetworkApplianceFirewallOneToManyNatRulesRequestRulesInnerPortRulesInner]**](UpdateNetworkApplianceFirewallOneToManyNatRulesRequestRulesInnerPortRulesInner.md) | An array of associated forwarding rules | 
**publicIp** | **String** | The IP address that will be used to access the internal resource from the WAN | 
**uplink** | **String** | The physical WAN interface on which the traffic will arrive (&#39;internet1&#39; or, if available, &#39;internet2&#39;) | 



## Enum: UplinkEnum


* `internet1` (value: `"internet1"`)

* `internet2` (value: `"internet2"`)




