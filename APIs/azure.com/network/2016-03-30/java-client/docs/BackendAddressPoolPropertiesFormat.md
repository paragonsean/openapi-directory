

# BackendAddressPoolPropertiesFormat

Properties of BackendAddressPool

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**backendIPConfigurations** | [**List&lt;NetworkInterfaceIPConfiguration&gt;**](NetworkInterfaceIPConfiguration.md) | Gets collection of references to IPs defined in NICs |  [optional] |
|**loadBalancingRules** | [**List&lt;SubResource&gt;**](SubResource.md) | Gets Load Balancing rules that use this Backend Address Pool |  [optional] |
|**outboundNatRule** | [**SubResource**](SubResource.md) |  |  [optional] |
|**provisioningState** | **String** | Provisioning state of the PublicIP resource Updating/Deleting/Failed |  [optional] |



