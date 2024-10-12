# NetworkManagementClient.ApplicationGatewayFrontendIPConfigurationPropertiesFormat

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**privateIPAddress** | **String** | PrivateIPAddress of the Network Interface IP Configuration | [optional] 
**privateIPAllocationMethod** | **String** | PrivateIP allocation method (Static/Dynamic) | [optional] 
**provisioningState** | **String** | Provisioning state of the PublicIP resource Updating/Deleting/Failed | [optional] 
**publicIPAddress** | [**SubResource**](SubResource.md) |  | [optional] 
**subnet** | [**SubResource**](SubResource.md) |  | [optional] 



## Enum: PrivateIPAllocationMethodEnum


* `Static` (value: `"Static"`)

* `Dynamic` (value: `"Dynamic"`)




