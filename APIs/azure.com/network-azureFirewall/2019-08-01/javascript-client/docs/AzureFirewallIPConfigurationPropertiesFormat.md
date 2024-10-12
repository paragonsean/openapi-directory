# NetworkManagementClient.AzureFirewallIPConfigurationPropertiesFormat

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**privateIPAddress** | **String** | The Firewall Internal Load Balancer IP to be used as the next hop in User Defined Routes. | [optional] [readonly] 
**provisioningState** | **String** | The current provisioning state. | [optional] [readonly] 
**publicIPAddress** | [**AzureFirewallIPConfigurationPropertiesFormatPublicIPAddress**](AzureFirewallIPConfigurationPropertiesFormatPublicIPAddress.md) |  | [optional] 
**subnet** | [**AzureFirewallIPConfigurationPropertiesFormatPublicIPAddress**](AzureFirewallIPConfigurationPropertiesFormatPublicIPAddress.md) |  | [optional] 



## Enum: ProvisioningStateEnum


* `Succeeded` (value: `"Succeeded"`)

* `Updating` (value: `"Updating"`)

* `Deleting` (value: `"Deleting"`)

* `Failed` (value: `"Failed"`)




