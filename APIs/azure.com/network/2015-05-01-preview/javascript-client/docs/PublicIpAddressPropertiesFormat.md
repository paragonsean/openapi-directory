# NetworkResourceProviderClient.PublicIpAddressPropertiesFormat

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dnsSettings** | [**PublicIpAddressDnsSettings**](PublicIpAddressDnsSettings.md) |  | [optional] 
**idleTimeoutInMinutes** | **Number** | Gets or sets the idle timeout of the public IP address | [optional] 
**ipAddress** | **String** | Gets the assigned public IP address | [optional] 
**ipConfiguration** | [**SubResource**](SubResource.md) |  | [optional] 
**provisioningState** | **String** | Gets or sets Provisioning state of the PublicIP resource Updating/Deleting/Failed | [optional] 
**publicIPAllocationMethod** | **String** | Gets or sets PublicIP allocation method (Static/Dynamic) | 
**resourceGuid** | **String** | Gets or sets resource guid property of the PublicIP resource | [optional] 



## Enum: PublicIPAllocationMethodEnum


* `Static` (value: `"Static"`)

* `Dynamic` (value: `"Dynamic"`)




