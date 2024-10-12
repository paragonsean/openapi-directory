# NetworkManagementClient.FrontendIPConfigurationPropertiesFormat

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inboundNatPools** | [**[SubResource]**](SubResource.md) | Read only. Inbound pools URIs that use this frontend IP | [optional] [readonly] 
**inboundNatRules** | [**[SubResource]**](SubResource.md) | Read only. Inbound rules URIs that use this frontend IP | [optional] [readonly] 
**loadBalancingRules** | [**[SubResource]**](SubResource.md) | Gets Load Balancing rules URIs that use this frontend IP | [optional] [readonly] 
**outboundNatRules** | [**[SubResource]**](SubResource.md) | Read only. Outbound rules URIs that use this frontend IP | [optional] [readonly] 
**privateIPAddress** | **String** | Gets or sets the privateIPAddress of the IP Configuration | [optional] 
**privateIPAllocationMethod** | **String** | Gets or sets PrivateIP allocation method | [optional] 
**provisioningState** | **String** | Gets provisioning state of the PublicIP resource Updating/Deleting/Failed | [optional] 
**publicIPAddress** | [**PublicIPAddress**](PublicIPAddress.md) |  | [optional] 
**subnet** | [**Subnet**](Subnet.md) |  | [optional] 



## Enum: PrivateIPAllocationMethodEnum


* `Static` (value: `"Static"`)

* `Dynamic` (value: `"Dynamic"`)




