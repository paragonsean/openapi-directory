

# PolicyAlternativeNameServerConfigTargetNameServer


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**forwardingPath** | [**ForwardingPathEnum**](#ForwardingPathEnum) | Forwarding path for this TargetNameServer. If unset or set to DEFAULT, Cloud DNS makes forwarding decisions based on address ranges; that is, RFC1918 addresses go to the VPC network, non-RFC1918 addresses go to the internet. When set to PRIVATE, Cloud DNS always sends queries through the VPC network for this target. |  [optional] |
|**ipv4Address** | **String** | IPv4 address to forward queries to. |  [optional] |
|**ipv6Address** | **String** | IPv6 address to forward to. Does not accept both fields (ipv4 &amp; ipv6) being populated. Public preview as of November 2022. |  [optional] |
|**kind** | **String** |  |  [optional] |



## Enum: ForwardingPathEnum

| Name | Value |
|---- | -----|
| DEFAULT | &quot;default&quot; |
| PRIVATE | &quot;private&quot; |



