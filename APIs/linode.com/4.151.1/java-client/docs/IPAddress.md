

# IPAddress

An IP address that exists in Linode's system, either IPv4 or IPv6. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**address** | **String** | The IP address.  |  [optional] [readonly] |
|**gateway** | **String** | The default gateway for this address.  |  [optional] [readonly] |
|**linodeId** | **Integer** | The ID of the Linode this address currently belongs to. For IPv4 addresses, this is by default the Linode that this address was assigned to on creation, and these addresses my be moved using the [/networking/ipv4/assign](/docs/api/networking/#ips-to-linodes-assign) endpoint. For SLAAC and link-local addresses, this value may not be changed.  |  [optional] [readonly] |
|**prefix** | **Integer** | The number of bits set in the subnet mask.  |  [optional] [readonly] |
|**_public** | **Boolean** | Whether this is a public or private IP address.  |  [optional] [readonly] |
|**rdns** | **String** | The reverse DNS assigned to this address. For public IPv4 addresses, this will be set to a default value provided by Linode if not explicitly set.  |  [optional] |
|**region** | **String** | The Region this IP address resides in.  |  [optional] [readonly] |
|**subnetMask** | **String** | The mask that separates host bits from network bits for this address.  |  [optional] [readonly] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of address this is.  |  [optional] [readonly] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| IPV4 | &quot;ipv4&quot; |
| IPV6 | &quot;ipv6&quot; |
| IPV6_POOL | &quot;ipv6/pool&quot; |
| IPV6_RANGE | &quot;ipv6/range&quot; |



