

# IpGroupPropertiesFormat

The IpGroups property information.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**firewalls** | [**List&lt;IpGroupPropertiesFormatFirewallsInner&gt;**](IpGroupPropertiesFormatFirewallsInner.md) | List of references to Azure resources that this IpGroups is associated with. |  [optional] [readonly] |
|**ipAddresses** | **List&lt;String&gt;** | IpAddresses/IpAddressPrefixes in the IpGroups resource. |  [optional] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | The current provisioning state. |  [optional] [readonly] |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| SUCCEEDED | &quot;Succeeded&quot; |
| UPDATING | &quot;Updating&quot; |
| DELETING | &quot;Deleting&quot; |
| FAILED | &quot;Failed&quot; |



