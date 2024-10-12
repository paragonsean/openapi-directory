# NetworkResourceProviderClient.FrontendIpConfigurationPropertiesFormat

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inboundNatPools** | [**[SubResource]**](SubResource.md) | Read only.Inbound pools URIs that use this frontend IP | [optional] 
**inboundNatRules** | [**[SubResource]**](SubResource.md) | Read only.Inbound rules URIs that use this frontend IP | [optional] 
**loadBalancingRules** | [**[SubResource]**](SubResource.md) | Gets Load Balancing rules URIs that use this frontend IP | [optional] 
**outboundNatRules** | [**[SubResource]**](SubResource.md) | Read only.Outbound rules URIs that use this frontend IP | [optional] 
**privateIPAddress** | **String** | Gets or sets the IP address of the Load Balancer.This is only specified if a specific private IP address shall be allocated from the subnet specified in subnetRef | [optional] 
**privateIPAllocationMethod** | **String** | Gets or sets PrivateIP allocation method (Static/Dynamic) | [optional] 
**provisioningState** | **String** | Gets or sets Provisioning state of the PublicIP resource Updating/Deleting/Failed | [optional] 
**publicIPAddress** | [**SubResource**](SubResource.md) |  | [optional] 
**subnet** | [**SubResource**](SubResource.md) |  | [optional] 



## Enum: PrivateIPAllocationMethodEnum


* `Static` (value: `"Static"`)

* `Dynamic` (value: `"Dynamic"`)




