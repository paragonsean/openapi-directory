# MerakiDashboardApi.UpdateNetworkVlanRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applianceIp** | **String** | The local IP of the appliance on the VLAN | [optional] 
**dhcpBootFilename** | **String** | DHCP boot option for boot filename | [optional] 
**dhcpBootNextServer** | **String** | DHCP boot option to direct boot clients to the server to load the boot file from | [optional] 
**dhcpBootOptionsEnabled** | **Boolean** | Use DHCP boot options specified in other properties | [optional] 
**dhcpHandling** | **String** | The appliance&#39;s handling of DHCP requests on this VLAN. One of: &#39;Run a DHCP server&#39;, &#39;Relay DHCP to another server&#39; or &#39;Do not respond to DHCP requests&#39; | [optional] 
**dhcpLeaseTime** | **String** | The term of DHCP leases if the appliance is running a DHCP server on this VLAN. One of: &#39;30 minutes&#39;, &#39;1 hour&#39;, &#39;4 hours&#39;, &#39;12 hours&#39;, &#39;1 day&#39; or &#39;1 week&#39; | [optional] 
**dhcpOptions** | [**[UpdateNetworkVlanRequestDhcpOptionsInner]**](UpdateNetworkVlanRequestDhcpOptionsInner.md) | The list of DHCP options that will be included in DHCP responses. Each object in the list should have \&quot;code\&quot;, \&quot;type\&quot;, and \&quot;value\&quot; properties. | [optional] 
**dhcpRelayServerIps** | **[String]** | The IPs of the DHCP servers that DHCP requests should be relayed to | [optional] 
**dnsNameservers** | **String** | The DNS nameservers used for DHCP responses, either \&quot;upstream_dns\&quot;, \&quot;google_dns\&quot;, \&quot;opendns\&quot;, or a newline seperated string of IP addresses or domain names | [optional] 
**fixedIpAssignments** | **Object** | The DHCP fixed IP assignments on the VLAN. This should be an object that contains mappings from MAC addresses to objects that themselves each contain \&quot;ip\&quot; and \&quot;name\&quot; string fields. See the sample request/response for more details. | [optional] 
**groupPolicyId** | **String** | The id of the desired group policy to apply to the VLAN | [optional] 
**name** | **String** | The name of the VLAN | [optional] 
**reservedIpRanges** | [**[UpdateNetworkStaticRouteRequestReservedIpRangesInner]**](UpdateNetworkStaticRouteRequestReservedIpRangesInner.md) | The DHCP reserved IP ranges on the VLAN | [optional] 
**subnet** | **String** | The subnet of the VLAN | [optional] 
**vpnNatSubnet** | **String** | The translated VPN subnet if VPN and VPN subnet translation are enabled on the VLAN | [optional] 



## Enum: DhcpHandlingEnum


* `Do not respond to DHCP requests` (value: `"Do not respond to DHCP requests"`)

* `Relay DHCP to another server` (value: `"Relay DHCP to another server"`)

* `Run a DHCP server` (value: `"Run a DHCP server"`)





## Enum: DhcpLeaseTimeEnum


* `1 day` (value: `"1 day"`)

* `1 hour` (value: `"1 hour"`)

* `1 week` (value: `"1 week"`)

* `12 hours` (value: `"12 hours"`)

* `30 minutes` (value: `"30 minutes"`)

* `4 hours` (value: `"4 hours"`)




