

# UpdateNetworkApplianceFirewallOneToOneNatRulesRequestRulesInnerAllowedInboundInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowedIps** | **List&lt;String&gt;** | An array of ranges of WAN IP addresses that are allowed to make inbound connections on the specified ports or port ranges, or &#39;any&#39; |  [optional] |
|**destinationPorts** | **List&lt;String&gt;** | An array of ports or port ranges that will be forwarded to the host on the LAN |  [optional] |
|**protocol** | [**ProtocolEnum**](#ProtocolEnum) | Either of the following: &#39;tcp&#39;, &#39;udp&#39;, &#39;icmp-ping&#39; or &#39;any&#39; |  [optional] |



## Enum: ProtocolEnum

| Name | Value |
|---- | -----|
| ANY | &quot;any&quot; |
| ICMP_PING | &quot;icmp-ping&quot; |
| TCP | &quot;tcp&quot; |
| UDP | &quot;udp&quot; |



