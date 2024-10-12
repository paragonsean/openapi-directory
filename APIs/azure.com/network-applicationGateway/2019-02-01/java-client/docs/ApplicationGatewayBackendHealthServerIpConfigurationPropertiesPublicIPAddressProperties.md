

# ApplicationGatewayBackendHealthServerIpConfigurationPropertiesPublicIPAddressProperties

Public IP address properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**ddosSettings** | [**ApplicationGatewayBackendHealthServerIpConfigurationPropertiesPublicIPAddressPropertiesDdosSettings**](ApplicationGatewayBackendHealthServerIpConfigurationPropertiesPublicIPAddressPropertiesDdosSettings.md) |  |  [optional] |
|**dnsSettings** | [**ApplicationGatewayBackendHealthServerIpConfigurationPropertiesPublicIPAddressPropertiesDnsSettings**](ApplicationGatewayBackendHealthServerIpConfigurationPropertiesPublicIPAddressPropertiesDnsSettings.md) |  |  [optional] |
|**idleTimeoutInMinutes** | **Integer** | The idle timeout of the public IP address. |  [optional] |
|**ipAddress** | **String** | The IP address associated with the public IP address resource. |  [optional] |
|**ipConfiguration** | **Items** |  |  [optional] |
|**ipTags** | [**List&lt;ApplicationGatewayBackendHealthServerIpConfigurationPropertiesPublicIPAddressPropertiesIpTagsInner&gt;**](ApplicationGatewayBackendHealthServerIpConfigurationPropertiesPublicIPAddressPropertiesIpTagsInner.md) | The list of tags associated with the public IP address. |  [optional] |
|**provisioningState** | **String** | The provisioning state of the PublicIP resource. Possible values are: &#39;Updating&#39;, &#39;Deleting&#39;, and &#39;Failed&#39;. |  [optional] |
|**publicIPAddressVersion** | **PrivateIPAddressVersion** |  |  [optional] |
|**publicIPAllocationMethod** | **PrivateIPAllocationMethod** |  |  [optional] |
|**publicIPPrefix** | **Model0** |  |  [optional] |
|**resourceGuid** | **String** | The resource GUID property of the public IP resource. |  [optional] |



