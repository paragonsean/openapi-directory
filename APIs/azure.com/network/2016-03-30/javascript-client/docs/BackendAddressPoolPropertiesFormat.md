# NetworkManagementClient.BackendAddressPoolPropertiesFormat

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backendIPConfigurations** | [**[NetworkInterfaceIPConfiguration]**](NetworkInterfaceIPConfiguration.md) | Gets collection of references to IPs defined in NICs | [optional] 
**loadBalancingRules** | [**[SubResource]**](SubResource.md) | Gets Load Balancing rules that use this Backend Address Pool | [optional] 
**outboundNatRule** | [**SubResource**](SubResource.md) |  | [optional] 
**provisioningState** | **String** | Provisioning state of the PublicIP resource Updating/Deleting/Failed | [optional] 


