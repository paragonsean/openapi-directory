

# SubnetOverride

Property overrides on a subnet of a virtual network.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**labSubnetName** | **String** | The name given to the subnet within the lab. |  [optional] |
|**resourceId** | **String** | The resource identifier of the subnet. |  [optional] |
|**useInVmCreationPermission** | [**UseInVmCreationPermissionEnum**](#UseInVmCreationPermissionEnum) | Indicates whether this subnet can be used during virtual machine creation. |  [optional] |
|**usePublicIpAddressPermission** | [**UsePublicIpAddressPermissionEnum**](#UsePublicIpAddressPermissionEnum) | Indicates whether public IP addresses can be assigned to virtual machines on this subnet. |  [optional] |



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



