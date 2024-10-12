# NetworkManagementClient.ApplicationGatewayBackendHealthServerIpConfigurationPropertiesVirtualNetworkTapsInnerPropertiesDestinationLoadBalancerFrontEndIPConfigurationProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inboundNatPools** | [**[Model0]**](Model0.md) | An array of references to inbound pools that use this frontend IP. | [optional] [readonly] 
**inboundNatRules** | [**[Model0]**](Model0.md) | An array of references to inbound rules that use this frontend IP. | [optional] [readonly] 
**loadBalancingRules** | [**[Model0]**](Model0.md) | An array of references to load balancing rules that use this frontend IP. | [optional] [readonly] 
**outboundRules** | [**[Model0]**](Model0.md) | An array of references to outbound rules that use this frontend IP. | [optional] [readonly] 
**privateIPAddress** | **String** | The private IP address of the IP configuration. | [optional] 
**privateIPAddressVersion** | [**PrivateIPAddressVersion**](PrivateIPAddressVersion.md) |  | [optional] 
**privateIPAllocationMethod** | [**PrivateIPAllocationMethod**](PrivateIPAllocationMethod.md) |  | [optional] 
**provisioningState** | [**ProvisioningState**](ProvisioningState.md) |  | [optional] 
**publicIPAddress** | [**PublicIPAddress**](PublicIPAddress.md) |  | [optional] 
**publicIPPrefix** | [**Model0**](Model0.md) |  | [optional] 
**subnet** | [**Subnet**](Subnet.md) |  | [optional] 


