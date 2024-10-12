

# BackendAddressPoolPropertiesFormat

Properties of BackendAddressPool

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**backendIPConfigurations** | [**List&lt;NetworkInterfaceIPConfiguration&gt;**](NetworkInterfaceIPConfiguration.md) | Gets collection of references to IPs defined in NICs |  [optional] [readonly] |
|**loadBalancingRules** | [**List&lt;SubResource&gt;**](SubResource.md) | Gets Load Balancing rules that use this Backend Address Pool |  [optional] [readonly] |
|**outboundNatRule** | [**SubResource**](SubResource.md) |  |  [optional] |
|**provisioningState** | **String** | Get provisioning state of the PublicIP resource Updating/Deleting/Failed |  [optional] |



