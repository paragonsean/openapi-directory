# MerakiDashboardApi.UpdateNetworkOneToOneNatRulesRequestRulesInnerAllowedInboundInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowedIps** | **[String]** | An array of ranges of WAN IP addresses that are allowed to make inbound connections on the specified ports or port ranges, or &#39;any&#39; | [optional] 
**destinationPorts** | **[String]** | An array of ports or port ranges that will be forwarded to the host on the LAN | [optional] 
**protocol** | **String** | Either of the following: &#39;tcp&#39;, &#39;udp&#39;, &#39;icmp-ping&#39; or &#39;any&#39; | [optional] 



## Enum: ProtocolEnum


* `any` (value: `"any"`)

* `icmp-ping` (value: `"icmp-ping"`)

* `tcp` (value: `"tcp"`)

* `udp` (value: `"udp"`)




