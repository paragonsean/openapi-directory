# LinodeApi.IPAddressesShareRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ips** | **[String]** | A list of secondary Linode IPs to share with the primary Linode. * Can include both IPv4 addresses and IPv6 ranges (omit /56 and /64 prefix lengths) * Can include both private and public IPv4 addresses. * You must have access to all of these addresses and they must be in the same Region as the primary Linode. * Enter an empty array to remove all shared IP addresses.  | 
**linodeId** | **Number** | The ID of the primary Linode that the addresses will be shared with.  | 


