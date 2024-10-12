# MerakiDashboardApi.UpdateNetworkSwitchStackRoutingInterfaceDhcpRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bootFileName** | **String** | The PXE boot server file name for the DHCP server running on the switch stack interface | [optional] 
**bootNextServer** | **String** | The PXE boot server IP for the DHCP server running on the switch stack interface | [optional] 
**bootOptionsEnabled** | **Boolean** | Enable DHCP boot options to provide PXE boot options configs for the dhcp server running on the switch stack interface | [optional] 
**dhcpLeaseTime** | **String** | The DHCP lease time config for the dhcp server running on switch stack interface (&#39;30 minutes&#39;, &#39;1 hour&#39;, &#39;4 hours&#39;, &#39;12 hours&#39;, &#39;1 day&#39; or &#39;1 week&#39;) | [optional] 
**dhcpMode** | **String** | The DHCP mode options for the switch stack interface (&#39;dhcpDisabled&#39;, &#39;dhcpRelay&#39; or &#39;dhcpServer&#39;) | [optional] 
**dhcpOptions** | [**[UpdateDeviceSwitchRoutingInterfaceDhcpRequestDhcpOptionsInner]**](UpdateDeviceSwitchRoutingInterfaceDhcpRequestDhcpOptionsInner.md) | Array of DHCP options consisting of code, type and value for the DHCP server running on the switch stack interface | [optional] 
**dhcpRelayServerIps** | **[String]** | The DHCP relay server IPs to which DHCP packets would get relayed for the switch stack interface | [optional] 
**dnsCustomNameservers** | **[String]** | The DHCP name server IPs when DHCP name server option is &#39;custom&#39; | [optional] 
**dnsNameserversOption** | **String** | The DHCP name server option for the dhcp server running on the switch stack interface (&#39;googlePublicDns&#39;, &#39;openDns&#39; or &#39;custom&#39;) | [optional] 
**fixedIpAssignments** | [**[UpdateDeviceSwitchRoutingInterfaceDhcpRequestFixedIpAssignmentsInner]**](UpdateDeviceSwitchRoutingInterfaceDhcpRequestFixedIpAssignmentsInner.md) | Array of DHCP fixed IP assignments for the DHCP server running on the switch stack interface | [optional] 
**reservedIpRanges** | [**[UpdateDeviceSwitchRoutingInterfaceDhcpRequestReservedIpRangesInner]**](UpdateDeviceSwitchRoutingInterfaceDhcpRequestReservedIpRangesInner.md) | Array of DHCP reserved IP assignments for the DHCP server running on the switch stack interface | [optional] 



## Enum: DhcpLeaseTimeEnum


* `1 day` (value: `"1 day"`)

* `1 hour` (value: `"1 hour"`)

* `1 week` (value: `"1 week"`)

* `12 hours` (value: `"12 hours"`)

* `30 minutes` (value: `"30 minutes"`)

* `4 hours` (value: `"4 hours"`)





## Enum: DhcpModeEnum


* `dhcpDisabled` (value: `"dhcpDisabled"`)

* `dhcpRelay` (value: `"dhcpRelay"`)

* `dhcpServer` (value: `"dhcpServer"`)





## Enum: DnsNameserversOptionEnum


* `custom` (value: `"custom"`)

* `googlePublicDns` (value: `"googlePublicDns"`)

* `openDns` (value: `"openDns"`)




