

# ApplicationGatewayBackendHealthServerIpConfigurationPropertiesPublicIPAddressProperties

Public IP address properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dnsSettings** | [**ApplicationGatewayBackendHealthServerIpConfigurationPropertiesPublicIPAddressPropertiesDnsSettings**](ApplicationGatewayBackendHealthServerIpConfigurationPropertiesPublicIPAddressPropertiesDnsSettings.md) |  |  [optional] |
|**idleTimeoutInMinutes** | **Integer** | The idle timeout of the public IP address. |  [optional] |
|**ipAddress** | **String** | The IP address associated with the public IP address resource. |  [optional] |
|**ipConfiguration** | **Items** |  |  [optional] |
|**provisioningState** | **String** | The provisioning state of the PublicIP resource. Possible values are: &#39;Updating&#39;, &#39;Deleting&#39;, and &#39;Failed&#39;. |  [optional] |
|**publicIPAddressVersion** | [**PublicIPAddressVersionEnum**](#PublicIPAddressVersionEnum) | The public IP address version. Possible values are: &#39;IPv4&#39; and &#39;IPv6&#39;. |  [optional] |
|**publicIPAllocationMethod** | [**PublicIPAllocationMethodEnum**](#PublicIPAllocationMethodEnum) | The public IP allocation method. Possible values are: &#39;Static&#39; and &#39;Dynamic&#39;. |  [optional] |
|**resourceGuid** | **String** | The resource GUID property of the public IP resource. |  [optional] |



## Enum: PublicIPAddressVersionEnum

| Name | Value |
|---- | -----|
| IPV4 | &quot;IPv4&quot; |
| IPV6 | &quot;IPv6&quot; |



## Enum: PublicIPAllocationMethodEnum

| Name | Value |
|---- | -----|
| STATIC | &quot;Static&quot; |
| DYNAMIC | &quot;Dynamic&quot; |



