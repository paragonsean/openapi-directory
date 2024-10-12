# NetworkManagementClient.IpGroupPropertiesFormat

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**firewalls** | [**[IpGroupPropertiesFormatFirewallsInner]**](IpGroupPropertiesFormatFirewallsInner.md) | List of references to Azure resources that this IpGroups is associated with. | [optional] [readonly] 
**ipAddresses** | **[String]** | IpAddresses/IpAddressPrefixes in the IpGroups resource. | [optional] 
**provisioningState** | **String** | The current provisioning state. | [optional] [readonly] 



## Enum: ProvisioningStateEnum


* `Succeeded` (value: `"Succeeded"`)

* `Updating` (value: `"Updating"`)

* `Deleting` (value: `"Deleting"`)

* `Failed` (value: `"Failed"`)




