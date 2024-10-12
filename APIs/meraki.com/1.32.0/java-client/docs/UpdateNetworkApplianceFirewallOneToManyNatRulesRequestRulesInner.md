

# UpdateNetworkApplianceFirewallOneToManyNatRulesRequestRulesInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**portRules** | [**List&lt;UpdateNetworkApplianceFirewallOneToManyNatRulesRequestRulesInnerPortRulesInner&gt;**](UpdateNetworkApplianceFirewallOneToManyNatRulesRequestRulesInnerPortRulesInner.md) | An array of associated forwarding rules |  |
|**publicIp** | **String** | The IP address that will be used to access the internal resource from the WAN |  |
|**uplink** | [**UplinkEnum**](#UplinkEnum) | The physical WAN interface on which the traffic will arrive (&#39;internet1&#39; or, if available, &#39;internet2&#39;) |  |



## Enum: UplinkEnum

| Name | Value |
|---- | -----|
| INTERNET1 | &quot;internet1&quot; |
| INTERNET2 | &quot;internet2&quot; |



