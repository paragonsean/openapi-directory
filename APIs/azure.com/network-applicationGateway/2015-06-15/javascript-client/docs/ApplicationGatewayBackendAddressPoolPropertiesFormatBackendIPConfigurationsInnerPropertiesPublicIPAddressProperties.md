# NetworkManagementClient.ApplicationGatewayBackendAddressPoolPropertiesFormatBackendIPConfigurationsInnerPropertiesPublicIPAddressProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dnsSettings** | [**ApplicationGatewayBackendAddressPoolPropertiesFormatBackendIPConfigurationsInnerPropertiesPublicIPAddressPropertiesDnsSettings**](ApplicationGatewayBackendAddressPoolPropertiesFormatBackendIPConfigurationsInnerPropertiesPublicIPAddressPropertiesDnsSettings.md) |  | [optional] 
**idleTimeoutInMinutes** | **Number** | The idle timeout of the public IP address. | [optional] 
**ipAddress** | **String** |  | [optional] 
**ipConfiguration** | [**Items**](Items.md) |  | [optional] 
**provisioningState** | **String** | The provisioning state of the PublicIP resource. Possible values are: &#39;Updating&#39;, &#39;Deleting&#39;, and &#39;Failed&#39;. | [optional] 
**publicIPAllocationMethod** | **String** | The public IP allocation method. Possible values are: &#39;Static&#39; and &#39;Dynamic&#39;. | [optional] 
**resourceGuid** | **String** | The resource GUID property of the public IP resource. | [optional] 



## Enum: PublicIPAllocationMethodEnum


* `Static` (value: `"Static"`)

* `Dynamic` (value: `"Dynamic"`)




