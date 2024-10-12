# BatchService.NetworkConfiguration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dynamicVNetAssignmentScope** | **String** |  | [optional] 
**endpointConfiguration** | [**PoolEndpointConfiguration**](PoolEndpointConfiguration.md) |  | [optional] 
**subnetId** | **String** | This is of the form /subscriptions/{subscription}/resourceGroups/{group}/providers/{provider}/virtualNetworks/{network}/subnets/{subnet}. The virtual network must be in the same region and subscription as the Azure Batch account. The specified subnet should have enough free IP addresses to accommodate the number of nodes in the pool. If the subnet doesn&#39;t have enough free IP addresses, the pool will partially allocate compute nodes, and a resize error will occur. For pools created with virtualMachineConfiguration only ARM virtual networks (&#39;Microsoft.Network/virtualNetworks&#39;) are supported, but for pools created with cloudServiceConfiguration both ARM and classic virtual networks are supported. For more details, see: https://docs.microsoft.com/en-us/azure/batch/batch-api-basics#virtual-network-vnet-and-firewall-configuration | [optional] 



## Enum: DynamicVNetAssignmentScopeEnum


* `none` (value: `"none"`)

* `job` (value: `"job"`)




