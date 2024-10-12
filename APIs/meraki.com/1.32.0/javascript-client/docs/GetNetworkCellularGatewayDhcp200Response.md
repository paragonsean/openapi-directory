# MerakiDashboardApi.GetNetworkCellularGatewayDhcp200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dhcpLeaseTime** | **String** | DHCP Lease time for all MG in the network. | [optional] 
**dnsCustomNameservers** | **[String]** | List of fixed IPs representing the the DNS Name servers when the mode is &#39;custom&#39;. | [optional] 
**dnsNameservers** | **String** | DNS name servers mode for all MG in the network. | [optional] 



## Enum: DhcpLeaseTimeEnum


* `1 day` (value: `"1 day"`)

* `1 hour` (value: `"1 hour"`)

* `1 week` (value: `"1 week"`)

* `12 hours` (value: `"12 hours"`)

* `30 minutes` (value: `"30 minutes"`)

* `4 hours` (value: `"4 hours"`)





## Enum: DnsNameserversEnum


* `custom` (value: `"custom"`)

* `google_dns` (value: `"google_dns"`)

* `opendns` (value: `"opendns"`)

* `upstream_dns` (value: `"upstream_dns"`)




