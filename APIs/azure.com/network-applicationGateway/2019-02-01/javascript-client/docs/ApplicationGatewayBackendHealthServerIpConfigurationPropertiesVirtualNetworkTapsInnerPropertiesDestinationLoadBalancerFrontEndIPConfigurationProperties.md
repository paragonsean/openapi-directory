# NetworkManagementClient.ApplicationGatewayBackendHealthServerIpConfigurationPropertiesVirtualNetworkTapsInnerPropertiesDestinationLoadBalancerFrontEndIPConfigurationProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inboundNatPools** | [**[Model0]**](Model0.md) | Read only. Inbound pools URIs that use this frontend IP. | [optional] [readonly] 
**inboundNatRules** | [**[Model0]**](Model0.md) | Read only. Inbound rules URIs that use this frontend IP. | [optional] [readonly] 
**loadBalancingRules** | [**[Model0]**](Model0.md) | Gets load balancing rules URIs that use this frontend IP. | [optional] [readonly] 
**outboundRules** | [**[Model0]**](Model0.md) | Read only. Outbound rules URIs that use this frontend IP. | [optional] [readonly] 
**privateIPAddress** | **String** | The private IP address of the IP configuration. | [optional] 
**privateIPAllocationMethod** | [**PrivateIPAllocationMethod**](PrivateIPAllocationMethod.md) |  | [optional] 
**provisioningState** | **String** | Gets the provisioning state of the public IP resource. Possible values are: &#39;Updating&#39;, &#39;Deleting&#39;, and &#39;Failed&#39;. | [optional] 
**publicIPAddress** | [**PublicIPAddress**](PublicIPAddress.md) |  | [optional] 
**publicIPPrefix** | [**Model0**](Model0.md) |  | [optional] 
**subnet** | [**Subnet**](Subnet.md) |  | [optional] 


