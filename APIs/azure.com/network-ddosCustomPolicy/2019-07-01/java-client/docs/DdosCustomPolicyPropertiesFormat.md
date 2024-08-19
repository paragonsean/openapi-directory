

# DdosCustomPolicyPropertiesFormat

DDoS custom policy properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**protocolCustomSettings** | [**List&lt;ProtocolCustomSettingsFormat&gt;**](ProtocolCustomSettingsFormat.md) | The protocol-specific DDoS policy customization parameters. |  [optional] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | The current provisioning state. |  [optional] [readonly] |
|**publicIPAddresses** | [**List&lt;DdosCustomPolicyPropertiesFormatPublicIPAddressesInner&gt;**](DdosCustomPolicyPropertiesFormatPublicIPAddressesInner.md) | The list of public IPs associated with the DDoS custom policy resource. This list is read-only. |  [optional] [readonly] |
|**resourceGuid** | **String** | The resource GUID property of the DDoS custom policy resource. It uniquely identifies the resource, even if the user changes its name or migrate the resource across subscriptions or resource groups. |  [optional] [readonly] |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| SUCCEEDED | &quot;Succeeded&quot; |
| UPDATING | &quot;Updating&quot; |
| DELETING | &quot;Deleting&quot; |
| FAILED | &quot;Failed&quot; |



