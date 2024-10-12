# NetworkManagementClient.ApplicationGatewayBackendHealthServerIpConfigurationPropertiesPublicIPAddressProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ddosSettings** | [**ApplicationGatewayBackendHealthServerIpConfigurationPropertiesPublicIPAddressPropertiesDdosSettings**](ApplicationGatewayBackendHealthServerIpConfigurationPropertiesPublicIPAddressPropertiesDdosSettings.md) |  | [optional] 
**dnsSettings** | [**ApplicationGatewayBackendHealthServerIpConfigurationPropertiesPublicIPAddressPropertiesDnsSettings**](ApplicationGatewayBackendHealthServerIpConfigurationPropertiesPublicIPAddressPropertiesDnsSettings.md) |  | [optional] 
**idleTimeoutInMinutes** | **Number** | The idle timeout of the public IP address. | [optional] 
**ipAddress** | **String** | The IP address associated with the public IP address resource. | [optional] 
**ipConfiguration** | [**Items**](Items.md) |  | [optional] 
**ipTags** | [**[ApplicationGatewayBackendHealthServerIpConfigurationPropertiesPublicIPAddressPropertiesIpTagsInner]**](ApplicationGatewayBackendHealthServerIpConfigurationPropertiesPublicIPAddressPropertiesIpTagsInner.md) | The list of tags associated with the public IP address. | [optional] 
**provisioningState** | **String** | The provisioning state of the PublicIP resource. Possible values are: &#39;Updating&#39;, &#39;Deleting&#39;, and &#39;Failed&#39;. | [optional] 
**publicIPAddressVersion** | [**PrivateIPAddressVersion**](PrivateIPAddressVersion.md) |  | [optional] 
**publicIPAllocationMethod** | [**PrivateIPAllocationMethod**](PrivateIPAllocationMethod.md) |  | [optional] 
**publicIPPrefix** | [**Model0**](Model0.md) |  | [optional] 
**resourceGuid** | **String** | The resource GUID property of the public IP resource. | [optional] 


