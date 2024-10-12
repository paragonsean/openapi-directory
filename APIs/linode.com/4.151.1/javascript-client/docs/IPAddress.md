# LinodeApi.IPAddress

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **String** | The IP address.  | [optional] [readonly] 
**gateway** | **String** | The default gateway for this address.  | [optional] [readonly] 
**linodeId** | **Number** | The ID of the Linode this address currently belongs to. For IPv4 addresses, this is by default the Linode that this address was assigned to on creation, and these addresses my be moved using the [/networking/ipv4/assign](/docs/api/networking/#ips-to-linodes-assign) endpoint. For SLAAC and link-local addresses, this value may not be changed.  | [optional] [readonly] 
**prefix** | **Number** | The number of bits set in the subnet mask.  | [optional] [readonly] 
**_public** | **Boolean** | Whether this is a public or private IP address.  | [optional] [readonly] 
**rdns** | **String** | The reverse DNS assigned to this address. For public IPv4 addresses, this will be set to a default value provided by Linode if not explicitly set.  | [optional] 
**region** | **String** | The Region this IP address resides in.  | [optional] [readonly] 
**subnetMask** | **String** | The mask that separates host bits from network bits for this address.  | [optional] [readonly] 
**type** | **String** | The type of address this is.  | [optional] [readonly] 



## Enum: TypeEnum


* `ipv4` (value: `"ipv4"`)

* `ipv6` (value: `"ipv6"`)

* `ipv6/pool` (value: `"ipv6/pool"`)

* `ipv6/range` (value: `"ipv6/range"`)




