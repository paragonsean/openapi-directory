# DevTestLabsClient.SubnetOverrideFragment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**labSubnetName** | **String** | The name given to the subnet within the lab. | [optional] 
**resourceId** | **String** | The resource ID of the subnet. | [optional] 
**sharedPublicIpAddressConfiguration** | [**SubnetSharedPublicIpAddressConfigurationFragment**](SubnetSharedPublicIpAddressConfigurationFragment.md) |  | [optional] 
**useInVmCreationPermission** | **String** | Indicates whether this subnet can be used during virtual machine creation (i.e. Allow, Deny). | [optional] 
**usePublicIpAddressPermission** | **String** | Indicates whether public IP addresses can be assigned to virtual machines on this subnet (i.e. Allow, Deny). | [optional] 
**virtualNetworkPoolName** | **String** | The virtual network pool associated with this subnet. | [optional] 



## Enum: UseInVmCreationPermissionEnum


* `Default` (value: `"Default"`)

* `Deny` (value: `"Deny"`)

* `Allow` (value: `"Allow"`)





## Enum: UsePublicIpAddressPermissionEnum


* `Default` (value: `"Default"`)

* `Deny` (value: `"Deny"`)

* `Allow` (value: `"Allow"`)




