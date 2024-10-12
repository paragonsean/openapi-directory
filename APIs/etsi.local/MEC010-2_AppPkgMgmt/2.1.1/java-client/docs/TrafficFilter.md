

# TrafficFilter


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dSCP** | **Integer** | Used to match all IPv4 packets that have the same DSCP. |  [optional] |
|**dstAddress** | **List&lt;String&gt;** | A IP address or a range of IP addresses.For IPv4, the IP address could be an IP address plus mask, or an individual IP address, or a range of IP addresses.For IPv6, the IP address could be an IP prefix, or a range of IP prefixes. |  [optional] |
|**dstPort** | **List&lt;String&gt;** | A port or a range of ports. |  [optional] |
|**dstTunnelPort** | **List&lt;String&gt;** | Used for GTP tunnel based traffic rule. |  [optional] |
|**protocol** | **List&lt;String&gt;** | Specify the protocol of the traffic filter. |  [optional] |
|**qCI** | **Integer** | Used to match all packets that have the same QCI. |  [optional] |
|**srcAddress** | **List&lt;String&gt;** | An IP address or a range of IP addresses.For IPv4, the IP address could be an IP address plus mask, or an individual IP address, or a range of IP addresses.For IPv6, the IP address could be an IP prefix, or a range of IP prefixes. |  [optional] |
|**srcPort** | **List&lt;String&gt;** | A port or a range of ports. |  [optional] |
|**srcTunnelAddress** | **List&lt;String&gt;** | Used for GTP tunnel based traffic rule. |  [optional] |
|**srcTunnelPort** | **List&lt;String&gt;** | Used for GTP tunnel based traffic rule. |  [optional] |
|**tC** | **Integer** | Used to match all IPv6 packets that have the same TC. |  [optional] |
|**tag** | **List&lt;String&gt;** | Used for tag based traffic rule. |  [optional] |
|**tgtTunnelAddress** | **List&lt;String&gt;** | Used for GTP tunnel based traffic rule. |  [optional] |



