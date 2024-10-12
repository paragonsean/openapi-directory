

# IPAddressPrivate

A private IPv4 address that exists in Linode's system. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**address** | **String** | The private IPv4 address.  |  [optional] [readonly] |
|**gateway** | **String** | The default gateway for this address.  |  [optional] [readonly] |
|**linodeId** | **Integer** | The ID of the Linode this address currently belongs to.  |  [optional] [readonly] |
|**prefix** | **Integer** | The number of bits set in the subnet mask.  |  [optional] [readonly] |
|**_public** | **Boolean** | Whether this is a public or private IP address.  |  [optional] [readonly] |
|**rdns** | **String** | The reverse DNS assigned to this address.  |  [optional] |
|**region** | **String** | The Region this address resides in.  |  [optional] [readonly] |
|**subnetMask** | **String** | The mask that separates host bits from network bits for this address.  |  [optional] [readonly] |
|**type** | **String** | The type of address this is.  |  [optional] [readonly] |



