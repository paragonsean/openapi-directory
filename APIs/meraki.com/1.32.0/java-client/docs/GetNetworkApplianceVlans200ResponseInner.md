

# GetNetworkApplianceVlans200ResponseInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**applianceIp** | **String** | The local IP of the appliance on the VLAN |  [optional] |
|**cidr** | **String** | CIDR of the pool of subnets. Applicable only for template network. Each network bound to the template will automatically pick a subnet from this pool to build its own VLAN. |  [optional] |
|**dhcpBootFilename** | **String** | DHCP boot option for boot filename |  [optional] |
|**dhcpBootNextServer** | **String** | DHCP boot option to direct boot clients to the server to load the boot file from |  [optional] |
|**dhcpBootOptionsEnabled** | **Boolean** | Use DHCP boot options specified in other properties |  [optional] |
|**dhcpHandling** | [**DhcpHandlingEnum**](#DhcpHandlingEnum) | The appliance&#39;s handling of DHCP requests on this VLAN. One of: &#39;Run a DHCP server&#39;, &#39;Relay DHCP to another server&#39; or &#39;Do not respond to DHCP requests&#39; |  [optional] |
|**dhcpLeaseTime** | [**DhcpLeaseTimeEnum**](#DhcpLeaseTimeEnum) | The term of DHCP leases if the appliance is running a DHCP server on this VLAN. One of: &#39;30 minutes&#39;, &#39;1 hour&#39;, &#39;4 hours&#39;, &#39;12 hours&#39;, &#39;1 day&#39; or &#39;1 week&#39; |  [optional] |
|**dhcpOptions** | [**List&lt;GetNetworkApplianceVlans200ResponseInnerDhcpOptionsInner&gt;**](GetNetworkApplianceVlans200ResponseInnerDhcpOptionsInner.md) | The list of DHCP options that will be included in DHCP responses. Each object in the list should have \&quot;code\&quot;, \&quot;type\&quot;, and \&quot;value\&quot; properties. |  [optional] |
|**dhcpRelayServerIps** | **List&lt;String&gt;** | The IPs of the DHCP servers that DHCP requests should be relayed to |  [optional] |
|**dnsNameservers** | **String** | The DNS nameservers used for DHCP responses, either \&quot;upstream_dns\&quot;, \&quot;google_dns\&quot;, \&quot;opendns\&quot;, or a newline seperated string of IP addresses or domain names |  [optional] |
|**fixedIpAssignments** | **Object** | The DHCP fixed IP assignments on the VLAN. This should be an object that contains mappings from MAC addresses to objects that themselves each contain \&quot;ip\&quot; and \&quot;name\&quot; string fields. See the sample request/response for more details. |  [optional] |
|**groupPolicyId** | **String** | The id of the desired group policy to apply to the VLAN |  [optional] |
|**id** | **String** | The VLAN ID of the VLAN |  [optional] |
|**interfaceId** | **String** | The interface ID of the VLAN |  [optional] |
|**ipv6** | [**GetNetworkApplianceVlans200ResponseInnerIpv6**](GetNetworkApplianceVlans200ResponseInnerIpv6.md) |  |  [optional] |
|**mandatoryDhcp** | [**GetNetworkApplianceVlans200ResponseInnerMandatoryDhcp**](GetNetworkApplianceVlans200ResponseInnerMandatoryDhcp.md) |  |  [optional] |
|**mask** | **Integer** | Mask used for the subnet of all bound to the template networks. Applicable only for template network. |  [optional] |
|**name** | **String** | The name of the VLAN |  [optional] |
|**reservedIpRanges** | [**List&lt;GetNetworkApplianceVlans200ResponseInnerReservedIpRangesInner&gt;**](GetNetworkApplianceVlans200ResponseInnerReservedIpRangesInner.md) | The DHCP reserved IP ranges on the VLAN |  [optional] |
|**subnet** | **String** | The subnet of the VLAN |  [optional] |
|**templateVlanType** | [**TemplateVlanTypeEnum**](#TemplateVlanTypeEnum) | Type of subnetting of the VLAN. Applicable only for template network. |  [optional] |
|**vpnNatSubnet** | **String** | The translated VPN subnet if VPN and VPN subnet translation are enabled on the VLAN |  [optional] |



## Enum: DhcpHandlingEnum

| Name | Value |
|---- | -----|
| DO_NOT_RESPOND_TO_DHCP_REQUESTS | &quot;Do not respond to DHCP requests&quot; |
| RELAY_DHCP_TO_ANOTHER_SERVER | &quot;Relay DHCP to another server&quot; |
| RUN_A_DHCP_SERVER | &quot;Run a DHCP server&quot; |



## Enum: DhcpLeaseTimeEnum

| Name | Value |
|---- | -----|
| _1_DAY | &quot;1 day&quot; |
| _1_HOUR | &quot;1 hour&quot; |
| _1_WEEK | &quot;1 week&quot; |
| _12_HOURS | &quot;12 hours&quot; |
| _30_MINUTES | &quot;30 minutes&quot; |
| _4_HOURS | &quot;4 hours&quot; |



## Enum: TemplateVlanTypeEnum

| Name | Value |
|---- | -----|
| SAME | &quot;same&quot; |
| UNIQUE | &quot;unique&quot; |



