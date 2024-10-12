

# ProxyConnectionInfo

For display only. Metadata associated with ProxyConnection.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**networkUri** | **String** | URI of the network where connection is proxied. |  [optional] |
|**newDestinationIp** | **String** | Destination IP address of a new connection. |  [optional] |
|**newDestinationPort** | **Integer** | Destination port of a new connection. Only valid when protocol is TCP or UDP. |  [optional] |
|**newSourceIp** | **String** | Source IP address of a new connection. |  [optional] |
|**newSourcePort** | **Integer** | Source port of a new connection. Only valid when protocol is TCP or UDP. |  [optional] |
|**oldDestinationIp** | **String** | Destination IP address of an original connection |  [optional] |
|**oldDestinationPort** | **Integer** | Destination port of an original connection. Only valid when protocol is TCP or UDP. |  [optional] |
|**oldSourceIp** | **String** | Source IP address of an original connection. |  [optional] |
|**oldSourcePort** | **Integer** | Source port of an original connection. Only valid when protocol is TCP or UDP. |  [optional] |
|**protocol** | **String** | IP protocol in string format, for example: \&quot;TCP\&quot;, \&quot;UDP\&quot;, \&quot;ICMP\&quot;. |  [optional] |
|**subnetUri** | **String** | Uri of proxy subnet. |  [optional] |



