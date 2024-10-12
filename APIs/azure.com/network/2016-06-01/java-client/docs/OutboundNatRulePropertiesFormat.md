

# OutboundNatRulePropertiesFormat

Outbound NAT pool of the load balancer

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allocatedOutboundPorts** | **Integer** | Gets or sets the number of outbound ports to be used for SNAT |  [optional] |
|**backendAddressPool** | [**SubResource**](SubResource.md) |  |  |
|**frontendIPConfigurations** | [**List&lt;SubResource&gt;**](SubResource.md) | Gets or sets Frontend IP addresses of the load balancer |  [optional] |
|**provisioningState** | **String** | Gets provisioning state of the PublicIP resource Updating/Deleting/Failed |  [optional] |



