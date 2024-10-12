

# DdosCustomPolicyPropertiesFormat

DDoS custom policy properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**protocolCustomSettings** | [**List&lt;ProtocolCustomSettingsFormat&gt;**](ProtocolCustomSettingsFormat.md) | The protocol-specific DDoS policy customization parameters. |  [optional] |
|**provisioningState** | **String** | The provisioning state of the DDoS custom policy resource. Possible values are: &#39;Succeeded&#39;, &#39;Updating&#39;, &#39;Deleting&#39;, and &#39;Failed&#39;. |  [optional] [readonly] |
|**publicIPAddresses** | [**List&lt;DdosCustomPolicyPropertiesFormatPublicIPAddressesInner&gt;**](DdosCustomPolicyPropertiesFormatPublicIPAddressesInner.md) | The list of public IPs associated with the DDoS custom policy resource. This list is read-only. |  [optional] [readonly] |
|**resourceGuid** | **String** | The resource GUID property of the DDoS custom policy resource. It uniquely identifies the resource, even if the user changes its name or migrate the resource across subscriptions or resource groups. |  [optional] [readonly] |



