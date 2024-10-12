# MerakiDashboardApi.UpdateNetworkApplianceFirewallOneToManyNatRulesRequestRulesInnerPortRulesInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowedIps** | **[String]** | Remote IP addresses or ranges that are permitted to access the internal resource via this port forwarding rule, or &#39;any&#39; | [optional] 
**localIp** | **String** | Local IP address to which traffic will be forwarded | [optional] 
**localPort** | **String** | Destination port of the forwarded traffic that will be sent from the MX to the specified host on the LAN. If you simply wish to forward the traffic without translating the port, this should be the same as the Public port | [optional] 
**name** | **String** | A description of the rule | [optional] 
**protocol** | **String** | &#39;tcp&#39; or &#39;udp&#39; | [optional] 
**publicPort** | **String** | Destination port of the traffic that is arriving on the WAN | [optional] 



## Enum: ProtocolEnum


* `tcp` (value: `"tcp"`)

* `udp` (value: `"udp"`)




