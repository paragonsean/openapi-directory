# NetworkManagementClient.LoadBalancerPropertiesFormat

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backendAddressPools** | [**[BackendAddressPool]**](BackendAddressPool.md) | Gets or sets Pools of backend IP addresses | [optional] 
**frontendIPConfigurations** | [**[FrontendIPConfiguration]**](FrontendIPConfiguration.md) | Gets or sets frontend IP addresses of the load balancer | [optional] 
**inboundNatPools** | [**[InboundNatPool]**](InboundNatPool.md) | Gets or sets inbound NAT pools | [optional] 
**inboundNatRules** | [**[InboundNatRule]**](InboundNatRule.md) | Gets or sets list of inbound rules | [optional] 
**loadBalancingRules** | [**[LoadBalancingRule]**](LoadBalancingRule.md) | Gets or sets load balancing rules | [optional] 
**outboundNatRules** | [**[OutboundNatRule]**](OutboundNatRule.md) | Gets or sets outbound NAT rules | [optional] 
**probes** | [**[Probe]**](Probe.md) | Gets or sets list of Load balancer probes | [optional] 
**provisioningState** | **String** | Gets provisioning state of the PublicIP resource Updating/Deleting/Failed | [optional] 
**resourceGuid** | **String** | Gets or sets resource guid property of the Load balancer resource | [optional] 


