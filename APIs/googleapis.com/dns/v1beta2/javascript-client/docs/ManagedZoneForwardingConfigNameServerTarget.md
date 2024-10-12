# CloudDnsApi.ManagedZoneForwardingConfigNameServerTarget

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**forwardingPath** | **String** | Forwarding path for this NameServerTarget. If unset or set to DEFAULT, Cloud DNS makes forwarding decisions based on IP address ranges; that is, RFC1918 addresses go to the VPC network, non-RFC1918 addresses go to the internet. When set to PRIVATE, Cloud DNS always sends queries through the VPC network for this target. | [optional] 
**ipv4Address** | **String** | IPv4 address of a target name server. | [optional] 
**ipv6Address** | **String** | IPv6 address of a target name server. Does not accept both fields (ipv4 &amp; ipv6) being populated. Public preview as of November 2022. | [optional] 
**kind** | **String** |  | [optional] [default to &#39;dns#managedZoneForwardingConfigNameServerTarget&#39;]



## Enum: ForwardingPathEnum


* `default` (value: `"default"`)

* `private` (value: `"private"`)




