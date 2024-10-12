

# FrontendIPConfigurationPropertiesFormat

Properties of Frontend IP Configuration of the load balancer

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**inboundNatPools** | [**List&lt;SubResource&gt;**](SubResource.md) | Read only. Inbound pools URIs that use this frontend IP |  [optional] [readonly] |
|**inboundNatRules** | [**List&lt;SubResource&gt;**](SubResource.md) | Read only. Inbound rules URIs that use this frontend IP |  [optional] [readonly] |
|**loadBalancingRules** | [**List&lt;SubResource&gt;**](SubResource.md) | Gets Load Balancing rules URIs that use this frontend IP |  [optional] [readonly] |
|**outboundNatRules** | [**List&lt;SubResource&gt;**](SubResource.md) | Read only. Outbound rules URIs that use this frontend IP |  [optional] [readonly] |
|**privateIPAddress** | **String** | Gets or sets the privateIPAddress of the IP Configuration |  [optional] |
|**privateIPAllocationMethod** | [**PrivateIPAllocationMethodEnum**](#PrivateIPAllocationMethodEnum) | Gets or sets PrivateIP allocation method |  [optional] |
|**provisioningState** | **String** | Gets provisioning state of the PublicIP resource Updating/Deleting/Failed |  [optional] |
|**publicIPAddress** | [**PublicIPAddress**](PublicIPAddress.md) |  |  [optional] |
|**subnet** | [**Subnet**](Subnet.md) |  |  [optional] |



## Enum: PrivateIPAllocationMethodEnum

| Name | Value |
|---- | -----|
| STATIC | &quot;Static&quot; |
| DYNAMIC | &quot;Dynamic&quot; |



