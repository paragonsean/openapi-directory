# BatchService.NetworkConfiguration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dynamicVNetAssignmentScope** | **String** |  | [optional] 
**endpointConfiguration** | [**PoolEndpointConfiguration**](PoolEndpointConfiguration.md) |  | [optional] 
**subnetId** | **String** | The virtual network must be in the same region and subscription as the Azure Batch Account. The specified subnet should have enough free IP addresses to accommodate the number of Compute Nodes in the Pool. If the subnet doesn&#39;t have enough free IP addresses, the Pool will partially allocate Nodes, and a resize error will occur. The &#39;MicrosoftAzureBatch&#39; service principal must have the &#39;Classic Virtual Machine Contributor&#39; Role-Based Access Control (RBAC) role for the specified VNet. The specified subnet must allow communication from the Azure Batch service to be able to schedule Tasks on the Nodes. This can be verified by checking if the specified VNet has any associated Network Security Groups (NSG). If communication to the Nodes in the specified subnet is denied by an NSG, then the Batch service will set the state of the Compute Nodes to unusable. For Pools created with virtualMachineConfiguration only ARM virtual networks (&#39;Microsoft.Network/virtualNetworks&#39;) are supported, but for Pools created with cloudServiceConfiguration both ARM and classic virtual networks are supported. If the specified VNet has any associated Network Security Groups (NSG), then a few reserved system ports must be enabled for inbound communication. For Pools created with a virtual machine configuration, enable ports 29876 and 29877, as well as port 22 for Linux and port 3389 for Windows. For Pools created with a cloud service configuration, enable ports 10100, 20100, and 30100. Also enable outbound connections to Azure Storage on port 443. For more details see: https://docs.microsoft.com/en-us/azure/batch/batch-api-basics#virtual-network-vnet-and-firewall-configuration | [optional] 



## Enum: DynamicVNetAssignmentScopeEnum


* `none` (value: `"none"`)

* `job` (value: `"job"`)




