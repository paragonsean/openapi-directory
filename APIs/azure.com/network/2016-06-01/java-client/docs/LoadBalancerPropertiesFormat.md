

# LoadBalancerPropertiesFormat

Properties of Load Balancer

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**backendAddressPools** | [**List&lt;BackendAddressPool&gt;**](BackendAddressPool.md) | Gets or sets Pools of backend IP addresses |  [optional] |
|**frontendIPConfigurations** | [**List&lt;FrontendIPConfiguration&gt;**](FrontendIPConfiguration.md) | Gets or sets frontend IP addresses of the load balancer |  [optional] |
|**inboundNatPools** | [**List&lt;InboundNatPool&gt;**](InboundNatPool.md) | Gets or sets inbound NAT pools |  [optional] |
|**inboundNatRules** | [**List&lt;InboundNatRule&gt;**](InboundNatRule.md) | Gets or sets list of inbound rules |  [optional] |
|**loadBalancingRules** | [**List&lt;LoadBalancingRule&gt;**](LoadBalancingRule.md) | Gets or sets load balancing rules |  [optional] |
|**outboundNatRules** | [**List&lt;OutboundNatRule&gt;**](OutboundNatRule.md) | Gets or sets outbound NAT rules |  [optional] |
|**probes** | [**List&lt;Probe&gt;**](Probe.md) | Gets or sets list of Load balancer probes |  [optional] |
|**provisioningState** | **String** | Gets provisioning state of the PublicIP resource Updating/Deleting/Failed |  [optional] |
|**resourceGuid** | **String** | Gets or sets resource guid property of the Load balancer resource |  [optional] |



