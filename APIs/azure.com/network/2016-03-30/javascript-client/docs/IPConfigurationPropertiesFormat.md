# NetworkManagementClient.IPConfigurationPropertiesFormat

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**privateIPAddress** | **String** | Gets or sets the privateIPAddress of the IP Configuration | [optional] 
**privateIPAllocationMethod** | **String** | Gets or sets PrivateIP allocation method (Static/Dynamic) | [optional] 
**provisioningState** | **String** | Gets or sets Provisioning state of the PublicIP resource Updating/Deleting/Failed | [optional] 
**publicIPAddress** | [**PublicIPAddress**](PublicIPAddress.md) |  | [optional] 
**subnet** | [**Subnet**](Subnet.md) |  | [optional] 



## Enum: PrivateIPAllocationMethodEnum


* `Static` (value: `"Static"`)

* `Dynamic` (value: `"Dynamic"`)




