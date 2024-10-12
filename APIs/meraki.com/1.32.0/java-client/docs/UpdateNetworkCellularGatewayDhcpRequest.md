

# UpdateNetworkCellularGatewayDhcpRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dhcpLeaseTime** | **String** | DHCP Lease time for all MG of the network. Possible values are &#39;30 minutes&#39;, &#39;1 hour&#39;, &#39;4 hours&#39;, &#39;12 hours&#39;, &#39;1 day&#39; or &#39;1 week&#39;. |  [optional] |
|**dnsCustomNameservers** | **List&lt;String&gt;** | list of fixed IPs representing the the DNS Name servers when the mode is &#39;custom&#39; |  [optional] |
|**dnsNameservers** | **String** | DNS name servers mode for all MG of the network. Possible values are: &#39;upstream_dns&#39;, &#39;google_dns&#39;, &#39;opendns&#39;, &#39;custom&#39;. |  [optional] |



