# NetworkManagementClient.BastionHostIPConfigurationPropertiesFormat

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**privateIPAllocationMethod** | **String** | IP address allocation method. | [optional] 
**provisioningState** | **String** | The current provisioning state. | [optional] [readonly] 
**publicIPAddress** | [**BastionHostIPConfigurationPropertiesFormatPublicIPAddress**](BastionHostIPConfigurationPropertiesFormatPublicIPAddress.md) |  | 
**subnet** | [**BastionHostIPConfigurationPropertiesFormatPublicIPAddress**](BastionHostIPConfigurationPropertiesFormatPublicIPAddress.md) |  | 



## Enum: PrivateIPAllocationMethodEnum


* `Static` (value: `"Static"`)

* `Dynamic` (value: `"Dynamic"`)





## Enum: ProvisioningStateEnum


* `Succeeded` (value: `"Succeeded"`)

* `Updating` (value: `"Updating"`)

* `Deleting` (value: `"Deleting"`)

* `Failed` (value: `"Failed"`)




