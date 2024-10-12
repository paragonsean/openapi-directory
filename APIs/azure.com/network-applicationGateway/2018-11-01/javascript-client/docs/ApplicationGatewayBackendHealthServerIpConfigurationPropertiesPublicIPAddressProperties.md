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
**publicIPAddressVersion** | **String** | The public IP address version. Possible values are: &#39;IPv4&#39; and &#39;IPv6&#39;. | [optional] 
**publicIPAllocationMethod** | **String** | The public IP allocation method. Possible values are: &#39;Static&#39; and &#39;Dynamic&#39;. | [optional] 
**publicIPPrefix** | [**Model0**](Model0.md) |  | [optional] 
**resourceGuid** | **String** | The resource GUID property of the public IP resource. | [optional] 



## Enum: PublicIPAddressVersionEnum


* `IPv4` (value: `"IPv4"`)

* `IPv6` (value: `"IPv6"`)





## Enum: PublicIPAllocationMethodEnum


* `Static` (value: `"Static"`)

* `Dynamic` (value: `"Dynamic"`)




