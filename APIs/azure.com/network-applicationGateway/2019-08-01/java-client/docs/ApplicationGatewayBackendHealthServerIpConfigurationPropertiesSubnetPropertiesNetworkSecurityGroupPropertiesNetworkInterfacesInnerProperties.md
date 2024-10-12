

# ApplicationGatewayBackendHealthServerIpConfigurationPropertiesSubnetPropertiesNetworkSecurityGroupPropertiesNetworkInterfacesInnerProperties

NetworkInterface properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dnsSettings** | [**ApplicationGatewayBackendHealthServerIpConfigurationPropertiesSubnetPropertiesNetworkSecurityGroupPropertiesNetworkInterfacesInnerPropertiesDnsSettings**](ApplicationGatewayBackendHealthServerIpConfigurationPropertiesSubnetPropertiesNetworkSecurityGroupPropertiesNetworkInterfacesInnerPropertiesDnsSettings.md) |  |  [optional] |
|**enableAcceleratedNetworking** | **Boolean** | If the network interface is accelerated networking enabled. |  [optional] |
|**enableIPForwarding** | **Boolean** | Indicates whether IP forwarding is enabled on this network interface. |  [optional] |
|**hostedWorkloads** | **List&lt;String&gt;** | A list of references to linked BareMetal resources. |  [optional] [readonly] |
|**ipConfigurations** | [**List&lt;ApplicationGatewayBackendHealthServerIpConfigurationPropertiesSubnetPropertiesNetworkSecurityGroupPropertiesNetworkInterfacesInnerPropertiesIpConfigurationsInner&gt;**](ApplicationGatewayBackendHealthServerIpConfigurationPropertiesSubnetPropertiesNetworkSecurityGroupPropertiesNetworkInterfacesInnerPropertiesIpConfigurationsInner.md) | A list of IPConfigurations of the network interface. |  [optional] |
|**macAddress** | **String** | The MAC address of the network interface. |  [optional] |
|**networkSecurityGroup** | **NetworkSecurityGroup** |  |  [optional] |
|**primary** | **Boolean** | Whether this is a primary network interface on a virtual machine. |  [optional] |
|**privateEndpoint** | **Items** |  |  [optional] |
|**provisioningState** | **ProvisioningState** |  |  [optional] |
|**resourceGuid** | **String** | The resource GUID property of the network interface resource. |  [optional] |
|**tapConfigurations** | [**List&lt;ApplicationGatewayBackendHealthServerIpConfigurationPropertiesSubnetPropertiesNetworkSecurityGroupPropertiesNetworkInterfacesInnerPropertiesTapConfigurationsInner&gt;**](ApplicationGatewayBackendHealthServerIpConfigurationPropertiesSubnetPropertiesNetworkSecurityGroupPropertiesNetworkInterfacesInnerPropertiesTapConfigurationsInner.md) | A list of TapConfigurations of the network interface. |  [optional] |
|**virtualMachine** | **Model0** |  |  [optional] |



