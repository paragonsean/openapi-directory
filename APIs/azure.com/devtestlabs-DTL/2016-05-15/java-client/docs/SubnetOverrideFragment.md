

# SubnetOverrideFragment

Property overrides on a subnet of a virtual network.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**labSubnetName** | **String** | The name given to the subnet within the lab. |  [optional] |
|**resourceId** | **String** | The resource ID of the subnet. |  [optional] |
|**sharedPublicIpAddressConfiguration** | [**SubnetSharedPublicIpAddressConfigurationFragment**](SubnetSharedPublicIpAddressConfigurationFragment.md) |  |  [optional] |
|**useInVmCreationPermission** | [**UseInVmCreationPermissionEnum**](#UseInVmCreationPermissionEnum) | Indicates whether this subnet can be used during virtual machine creation (i.e. Allow, Deny). |  [optional] |
|**usePublicIpAddressPermission** | [**UsePublicIpAddressPermissionEnum**](#UsePublicIpAddressPermissionEnum) | Indicates whether public IP addresses can be assigned to virtual machines on this subnet (i.e. Allow, Deny). |  [optional] |
|**virtualNetworkPoolName** | **String** | The virtual network pool associated with this subnet. |  [optional] |



## Enum: UseInVmCreationPermissionEnum

| Name | Value |
|---- | -----|
| DEFAULT | &quot;Default&quot; |
| DENY | &quot;Deny&quot; |
| ALLOW | &quot;Allow&quot; |



## Enum: UsePublicIpAddressPermissionEnum

| Name | Value |
|---- | -----|
| DEFAULT | &quot;Default&quot; |
| DENY | &quot;Deny&quot; |
| ALLOW | &quot;Allow&quot; |



