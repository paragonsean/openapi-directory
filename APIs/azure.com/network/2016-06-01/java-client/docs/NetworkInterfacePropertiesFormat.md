

# NetworkInterfacePropertiesFormat

NetworkInterface properties. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dnsSettings** | [**NetworkInterfaceDnsSettings**](NetworkInterfaceDnsSettings.md) |  |  [optional] |
|**enableIPForwarding** | **Boolean** | Gets or sets whether IPForwarding is enabled on the NIC |  [optional] |
|**ipConfigurations** | [**List&lt;NetworkInterfaceIPConfiguration&gt;**](NetworkInterfaceIPConfiguration.md) | Gets or sets list of IPConfigurations of the network interface |  [optional] |
|**macAddress** | **String** | Gets the MAC address of the network interface |  [optional] |
|**networkSecurityGroup** | [**NetworkSecurityGroup**](NetworkSecurityGroup.md) |  |  [optional] |
|**primary** | **Boolean** | Gets whether this is a primary NIC on a virtual machine |  [optional] |
|**provisioningState** | **String** | Gets provisioning state of the PublicIP resource Updating/Deleting/Failed |  [optional] |
|**resourceGuid** | **String** | Gets or sets resource guid property of the network interface resource |  [optional] |
|**virtualMachine** | [**SubResource**](SubResource.md) |  |  [optional] |



