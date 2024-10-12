

# ApplicationGatewayBackendAddressPoolPropertiesFormatBackendIPConfigurationsInnerPropertiesSubnetPropertiesNetworkSecurityGroupProperties

Network Security Group resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**defaultSecurityRules** | **List&lt;Items&gt;** | The default security rules of network security group. |  [optional] |
|**networkInterfaces** | [**List&lt;ApplicationGatewayBackendAddressPoolPropertiesFormatBackendIPConfigurationsInnerPropertiesSubnetPropertiesNetworkSecurityGroupPropertiesNetworkInterfacesInner&gt;**](ApplicationGatewayBackendAddressPoolPropertiesFormatBackendIPConfigurationsInnerPropertiesSubnetPropertiesNetworkSecurityGroupPropertiesNetworkInterfacesInner.md) | A collection of references to network interfaces. |  [optional] |
|**provisioningState** | **String** | The provisioning state of the public IP resource. Possible values are: &#39;Updating&#39;, &#39;Deleting&#39;, and &#39;Failed&#39;. |  [optional] |
|**resourceGuid** | **String** | The resource GUID property of the network security group resource. |  [optional] |
|**securityRules** | [**List&lt;ApplicationGatewayBackendAddressPoolPropertiesFormatBackendIPConfigurationsInnerPropertiesSubnetPropertiesNetworkSecurityGroupPropertiesSecurityRulesInner&gt;**](ApplicationGatewayBackendAddressPoolPropertiesFormatBackendIPConfigurationsInnerPropertiesSubnetPropertiesNetworkSecurityGroupPropertiesSecurityRulesInner.md) | A collection of security rules of the network security group. |  [optional] |
|**subnets** | **List&lt;Subnet&gt;** | A collection of references to subnets. |  [optional] |



