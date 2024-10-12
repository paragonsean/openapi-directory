

# UpdateNetworkApplianceFirewallPortForwardingRulesRequestRulesInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowedIps** | **List&lt;String&gt;** | An array of ranges of WAN IP addresses that are allowed to make inbound connections on the specified ports or port ranges (or any) |  |
|**lanIp** | **String** | The IP address of the server or device that hosts the internal resource that you wish to make available on the WAN |  |
|**localPort** | **String** | A port or port ranges that will receive the forwarded traffic from the WAN |  |
|**name** | **String** | A descriptive name for the rule |  [optional] |
|**protocol** | [**ProtocolEnum**](#ProtocolEnum) | TCP or UDP |  |
|**publicPort** | **String** | A port or port ranges that will be forwarded to the host on the LAN |  |
|**uplink** | [**UplinkEnum**](#UplinkEnum) | The physical WAN interface on which the traffic will arrive (&#39;internet1&#39; or, if available, &#39;internet2&#39; or &#39;both&#39;) |  [optional] |



## Enum: ProtocolEnum

| Name | Value |
|---- | -----|
| TCP | &quot;tcp&quot; |
| UDP | &quot;udp&quot; |



## Enum: UplinkEnum

| Name | Value |
|---- | -----|
| BOTH | &quot;both&quot; |
| INTERNET1 | &quot;internet1&quot; |
| INTERNET2 | &quot;internet2&quot; |



