

# GetNetworkCellularGatewayDhcp200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dhcpLeaseTime** | [**DhcpLeaseTimeEnum**](#DhcpLeaseTimeEnum) | DHCP Lease time for all MG in the network. |  [optional] |
|**dnsCustomNameservers** | **List&lt;String&gt;** | List of fixed IPs representing the the DNS Name servers when the mode is &#39;custom&#39;. |  [optional] |
|**dnsNameservers** | [**DnsNameserversEnum**](#DnsNameserversEnum) | DNS name servers mode for all MG in the network. |  [optional] |



## Enum: DhcpLeaseTimeEnum

| Name | Value |
|---- | -----|
| _1_DAY | &quot;1 day&quot; |
| _1_HOUR | &quot;1 hour&quot; |
| _1_WEEK | &quot;1 week&quot; |
| _12_HOURS | &quot;12 hours&quot; |
| _30_MINUTES | &quot;30 minutes&quot; |
| _4_HOURS | &quot;4 hours&quot; |



## Enum: DnsNameserversEnum

| Name | Value |
|---- | -----|
| CUSTOM | &quot;custom&quot; |
| GOOGLE_DNS | &quot;google_dns&quot; |
| OPENDNS | &quot;opendns&quot; |
| UPSTREAM_DNS | &quot;upstream_dns&quot; |



