# SiteRecoveryManagementClient.VMNicDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enableAcceleratedNetworkingOnRecovery** | **Boolean** | A value indicating whether the NIC has accelerated networking enabled. | [optional] 
**enableAcceleratedNetworkingOnTfo** | **Boolean** | Whether the test failover NIC has accelerated networking enabled. | [optional] 
**ipAddressType** | **String** | Ip address type. | [optional] 
**nicId** | **String** | The nic Id. | [optional] 
**primaryNicStaticIPAddress** | **String** | Primary nic static IP address. | [optional] 
**recoveryLBBackendAddressPoolIds** | **[String]** | The target backend address pools for the NIC. | [optional] 
**recoveryNetworkSecurityGroupId** | **String** | The id of the NSG associated with the NIC. | [optional] 
**recoveryNicIpAddressType** | **String** | IP allocation type for recovery VM. | [optional] 
**recoveryPublicIpAddressId** | **String** | The id of the public IP address resource associated with the NIC. | [optional] 
**recoveryVMNetworkId** | **String** | Recovery VM network Id. | [optional] 
**recoveryVMSubnetName** | **String** | Recovery VM subnet name. | [optional] 
**replicaNicId** | **String** | The replica nic Id. | [optional] 
**replicaNicStaticIPAddress** | **String** | Replica nic static IP address. | [optional] 
**selectionType** | **String** | Selection type for failover. | [optional] 
**sourceNicArmId** | **String** | The source nic ARM Id. | [optional] 
**tfoIPConfigs** | [**[IPConfig]**](IPConfig.md) | The IP configurations to be used by NIC during test failover. | [optional] 
**tfoNetworkSecurityGroupId** | **String** | The NSG to be used by NIC during test failover. | [optional] 
**tfoVMNetworkId** | **String** | The network to be used by NIC during test failover. | [optional] 
**tfoVMSubnetName** | **String** | The subnet to be used by NIC during test failover. | [optional] 
**vMNetworkName** | **String** | VM network name. | [optional] 
**vMSubnetName** | **String** | VM subnet name. | [optional] 


