# NetworkManagementClient.ApplicationGatewayBackendAddressPoolPropertiesFormat

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backendAddresses** | [**[ApplicationGatewayBackendAddress]**](ApplicationGatewayBackendAddress.md) | Backend addresses. | [optional] 
**backendIPConfigurations** | [**[ApplicationGatewayBackendHealthServerIpConfiguration]**](ApplicationGatewayBackendHealthServerIpConfiguration.md) | Collection of references to IPs defined in network interfaces. | [optional] 
**provisioningState** | **String** | The current provisioning state. | [optional] [readonly] 



## Enum: ProvisioningStateEnum


* `Succeeded` (value: `"Succeeded"`)

* `Updating` (value: `"Updating"`)

* `Deleting` (value: `"Deleting"`)

* `Failed` (value: `"Failed"`)




