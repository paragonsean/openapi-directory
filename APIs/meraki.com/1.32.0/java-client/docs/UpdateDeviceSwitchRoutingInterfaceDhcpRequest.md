

# UpdateDeviceSwitchRoutingInterfaceDhcpRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bootFileName** | **String** | The PXE boot server filename for the DHCP server running on the switch interface |  [optional] |
|**bootNextServer** | **String** | The PXE boot server IP for the DHCP server running on the switch interface |  [optional] |
|**bootOptionsEnabled** | **Boolean** | Enable DHCP boot options to provide PXE boot options configs for the dhcp server running on the switch interface |  [optional] |
|**dhcpLeaseTime** | [**DhcpLeaseTimeEnum**](#DhcpLeaseTimeEnum) | The DHCP lease time config for the dhcp server running on switch interface (&#39;30 minutes&#39;, &#39;1 hour&#39;, &#39;4 hours&#39;, &#39;12 hours&#39;, &#39;1 day&#39; or &#39;1 week&#39;) |  [optional] |
|**dhcpMode** | [**DhcpModeEnum**](#DhcpModeEnum) | The DHCP mode options for the switch interface (&#39;dhcpDisabled&#39;, &#39;dhcpRelay&#39; or &#39;dhcpServer&#39;) |  [optional] |
|**dhcpOptions** | [**List&lt;UpdateDeviceSwitchRoutingInterfaceDhcpRequestDhcpOptionsInner&gt;**](UpdateDeviceSwitchRoutingInterfaceDhcpRequestDhcpOptionsInner.md) | Array of DHCP options consisting of code, type and value for the DHCP server running on the switch interface |  [optional] |
|**dhcpRelayServerIps** | **List&lt;String&gt;** | The DHCP relay server IPs to which DHCP packets would get relayed for the switch interface |  [optional] |
|**dnsCustomNameservers** | **List&lt;String&gt;** | The DHCP name server IPs when DHCP name server option is &#39;custom&#39; |  [optional] |
|**dnsNameserversOption** | [**DnsNameserversOptionEnum**](#DnsNameserversOptionEnum) | The DHCP name server option for the dhcp server running on the switch interface (&#39;googlePublicDns&#39;, &#39;openDns&#39; or &#39;custom&#39;) |  [optional] |
|**fixedIpAssignments** | [**List&lt;UpdateDeviceSwitchRoutingInterfaceDhcpRequestFixedIpAssignmentsInner&gt;**](UpdateDeviceSwitchRoutingInterfaceDhcpRequestFixedIpAssignmentsInner.md) | Array of DHCP fixed IP assignments for the DHCP server running on the switch interface |  [optional] |
|**reservedIpRanges** | [**List&lt;UpdateDeviceSwitchRoutingInterfaceDhcpRequestReservedIpRangesInner&gt;**](UpdateDeviceSwitchRoutingInterfaceDhcpRequestReservedIpRangesInner.md) | Array of DHCP reserved IP assignments for the DHCP server running on the switch interface |  [optional] |



## Enum: DhcpLeaseTimeEnum

| Name | Value |
|---- | -----|
| _1_DAY | &quot;1 day&quot; |
| _1_HOUR | &quot;1 hour&quot; |
| _1_WEEK | &quot;1 week&quot; |
| _12_HOURS | &quot;12 hours&quot; |
| _30_MINUTES | &quot;30 minutes&quot; |
| _4_HOURS | &quot;4 hours&quot; |



## Enum: DhcpModeEnum

| Name | Value |
|---- | -----|
| DHCP_DISABLED | &quot;dhcpDisabled&quot; |
| DHCP_RELAY | &quot;dhcpRelay&quot; |
| DHCP_SERVER | &quot;dhcpServer&quot; |



## Enum: DnsNameserversOptionEnum

| Name | Value |
|---- | -----|
| CUSTOM | &quot;custom&quot; |
| GOOGLE_PUBLIC_DNS | &quot;googlePublicDns&quot; |
| OPEN_DNS | &quot;openDns&quot; |



