# NetworkManagementClient.PrivateLinkServiceIpConfigurationProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**primary** | **Boolean** | Whether the ip configuration is primary or not. | [optional] 
**privateIPAddress** | **String** | The private IP address of the IP configuration. | [optional] 
**privateIPAddressVersion** | **String** | IP address version. | [optional] 
**privateIPAllocationMethod** | **String** | IP address allocation method. | [optional] 
**provisioningState** | **String** | The current provisioning state. | [optional] [readonly] 
**subnet** | [**PrivateLinkServiceIpConfigurationPropertiesSubnet**](PrivateLinkServiceIpConfigurationPropertiesSubnet.md) |  | [optional] 



## Enum: PrivateIPAddressVersionEnum


* `IPv4` (value: `"IPv4"`)

* `IPv6` (value: `"IPv6"`)





## Enum: PrivateIPAllocationMethodEnum


* `Static` (value: `"Static"`)

* `Dynamic` (value: `"Dynamic"`)





## Enum: ProvisioningStateEnum


* `Succeeded` (value: `"Succeeded"`)

* `Updating` (value: `"Updating"`)

* `Deleting` (value: `"Deleting"`)

* `Failed` (value: `"Failed"`)




