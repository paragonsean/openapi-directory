# NetworkManagementClient.DdosCustomPolicyPropertiesFormat

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**protocolCustomSettings** | [**[ProtocolCustomSettingsFormat]**](ProtocolCustomSettingsFormat.md) | The protocol-specific DDoS policy customization parameters. | [optional] 
**provisioningState** | **String** | The current provisioning state. | [optional] [readonly] 
**publicIPAddresses** | [**[DdosCustomPolicyPropertiesFormatPublicIPAddressesInner]**](DdosCustomPolicyPropertiesFormatPublicIPAddressesInner.md) | The list of public IPs associated with the DDoS custom policy resource. This list is read-only. | [optional] [readonly] 
**resourceGuid** | **String** | The resource GUID property of the DDoS custom policy resource. It uniquely identifies the resource, even if the user changes its name or migrate the resource across subscriptions or resource groups. | [optional] [readonly] 



## Enum: ProvisioningStateEnum


* `Succeeded` (value: `"Succeeded"`)

* `Updating` (value: `"Updating"`)

* `Deleting` (value: `"Deleting"`)

* `Failed` (value: `"Failed"`)




