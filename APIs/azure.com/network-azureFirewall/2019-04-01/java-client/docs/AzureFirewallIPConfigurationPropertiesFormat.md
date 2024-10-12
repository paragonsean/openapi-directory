

# AzureFirewallIPConfigurationPropertiesFormat

Properties of IP configuration of an Azure Firewall.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**privateIPAddress** | **String** | The Firewall Internal Load Balancer IP to be used as the next hop in User Defined Routes. |  [optional] [readonly] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | The current provisioning state. |  [optional] [readonly] |
|**publicIPAddress** | [**AzureFirewallIPConfigurationPropertiesFormatPublicIPAddress**](AzureFirewallIPConfigurationPropertiesFormatPublicIPAddress.md) |  |  [optional] |
|**subnet** | [**AzureFirewallIPConfigurationPropertiesFormatPublicIPAddress**](AzureFirewallIPConfigurationPropertiesFormatPublicIPAddress.md) |  |  [optional] |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| SUCCEEDED | &quot;Succeeded&quot; |
| UPDATING | &quot;Updating&quot; |
| DELETING | &quot;Deleting&quot; |
| FAILED | &quot;Failed&quot; |



