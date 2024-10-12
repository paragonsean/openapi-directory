# SiteRecoveryManagementClient.VMNicInputDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enableAcceleratedNetworkingOnRecovery** | **Boolean** | Whether the NIC has accelerated networking enabled. | [optional] 
**enableAcceleratedNetworkingOnTfo** | **Boolean** | Whether the test NIC has accelerated networking enabled. | [optional] 
**nicId** | **String** | The nic Id. | [optional] 
**recoveryLBBackendAddressPoolIds** | **[String]** | The target backend address pools for the NIC. | [optional] 
**recoveryNetworkSecurityGroupId** | **String** | The id of the NSG associated with the NIC. | [optional] 
**recoveryPublicIpAddressId** | **String** | The id of the public IP address resource associated with the NIC. | [optional] 
**recoveryVMSubnetName** | **String** | Recovery VM subnet name. | [optional] 
**replicaNicStaticIPAddress** | **String** | Replica nic static IP address. | [optional] 
**selectionType** | **String** | Selection type for failover. | [optional] 
**tfoIPConfigs** | [**[IPConfig]**](IPConfig.md) | The IP configurations to be used by NIC during test failover. | [optional] 
**tfoNetworkSecurityGroupId** | **String** | The NSG to be used by NIC during test failover. | [optional] 
**tfoVMSubnetName** | **String** | The subnet to be used by NIC during test failover. | [optional] 


