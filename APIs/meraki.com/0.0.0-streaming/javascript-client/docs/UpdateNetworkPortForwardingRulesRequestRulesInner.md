# MerakiDashboardApi.UpdateNetworkPortForwardingRulesRequestRulesInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowedIps** | **[String]** | An array of ranges of WAN IP addresses that are allowed to make inbound connections on the specified ports or port ranges (or any) | 
**lanIp** | **String** | The IP address of the server or device that hosts the internal resource that you wish to make available on the WAN | 
**localPort** | **String** | A port or port ranges that will receive the forwarded traffic from the WAN | 
**name** | **String** | A descriptive name for the rule | [optional] 
**protocol** | **String** | TCP or UDP | 
**publicPort** | **String** | A port or port ranges that will be forwarded to the host on the LAN | 
**uplink** | **String** | The physical WAN interface on which the traffic will arrive (&#39;internet1&#39; or, if available, &#39;internet2&#39; or &#39;both&#39;) | [optional] 



## Enum: ProtocolEnum


* `tcp` (value: `"tcp"`)

* `udp` (value: `"udp"`)





## Enum: UplinkEnum


* `both` (value: `"both"`)

* `internet1` (value: `"internet1"`)

* `internet2` (value: `"internet2"`)




