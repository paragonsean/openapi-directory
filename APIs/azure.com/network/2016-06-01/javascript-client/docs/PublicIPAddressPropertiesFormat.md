# NetworkManagementClient.PublicIPAddressPropertiesFormat

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dnsSettings** | [**PublicIPAddressDnsSettings**](PublicIPAddressDnsSettings.md) |  | [optional] 
**idleTimeoutInMinutes** | **Number** | Gets or sets the idle timeout of the public IP address | [optional] 
**ipAddress** | **String** |  | [optional] 
**ipConfiguration** | [**IPConfiguration**](IPConfiguration.md) |  | [optional] 
**provisioningState** | **String** | Gets provisioning state of the PublicIP resource Updating/Deleting/Failed | [optional] 
**publicIPAddressVersion** | **String** | Gets or sets PublicIP address version (IPv4/IPv6) | [optional] 
**publicIPAllocationMethod** | **String** | Gets or sets PublicIP allocation method (Static/Dynamic) | [optional] 
**resourceGuid** | **String** | Gets or sets resource guid property of the PublicIP resource | [optional] 



## Enum: PublicIPAddressVersionEnum


* `IPv4` (value: `"IPv4"`)

* `IPv6` (value: `"IPv6"`)





## Enum: PublicIPAllocationMethodEnum


* `Static` (value: `"Static"`)

* `Dynamic` (value: `"Dynamic"`)




