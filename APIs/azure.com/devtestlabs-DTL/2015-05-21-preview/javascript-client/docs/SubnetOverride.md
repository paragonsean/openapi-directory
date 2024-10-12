# DevTestLabsClient.SubnetOverride

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**labSubnetName** | **String** | The name given to the subnet within the lab. | [optional] 
**resourceId** | **String** | The resource identifier of the subnet. | [optional] 
**useInVmCreationPermission** | **String** | Indicates whether this subnet can be used during virtual machine creation. | [optional] 
**usePublicIpAddressPermission** | **String** | Indicates whether public IP addresses can be assigned to virtual machines on this subnet. | [optional] 



## Enum: UseInVmCreationPermissionEnum


* `Default` (value: `"Default"`)

* `Deny` (value: `"Deny"`)

* `Allow` (value: `"Allow"`)





## Enum: UsePublicIpAddressPermissionEnum


* `Default` (value: `"Default"`)

* `Deny` (value: `"Deny"`)

* `Allow` (value: `"Allow"`)




