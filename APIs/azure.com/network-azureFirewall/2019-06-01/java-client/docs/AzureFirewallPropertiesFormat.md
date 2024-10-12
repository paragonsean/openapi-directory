

# AzureFirewallPropertiesFormat

Properties of the Azure Firewall.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**applicationRuleCollections** | [**List&lt;AzureFirewallApplicationRuleCollection&gt;**](AzureFirewallApplicationRuleCollection.md) | Collection of application rule collections used by Azure Firewall. |  [optional] |
|**firewallPolicy** | [**AzureFirewallIPConfigurationPropertiesFormatPublicIPAddress**](AzureFirewallIPConfigurationPropertiesFormatPublicIPAddress.md) |  |  [optional] |
|**hubIpAddresses** | [**HubIPAddresses**](HubIPAddresses.md) |  |  [optional] |
|**ipConfigurations** | [**List&lt;AzureFirewallIPConfiguration&gt;**](AzureFirewallIPConfiguration.md) | IP configuration of the Azure Firewall resource. |  [optional] |
|**natRuleCollections** | [**List&lt;AzureFirewallNatRuleCollection&gt;**](AzureFirewallNatRuleCollection.md) | Collection of NAT rule collections used by Azure Firewall. |  [optional] |
|**networkRuleCollections** | [**List&lt;AzureFirewallNetworkRuleCollection&gt;**](AzureFirewallNetworkRuleCollection.md) | Collection of network rule collections used by Azure Firewall. |  [optional] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | The current provisioning state. |  [optional] [readonly] |
|**threatIntelMode** | **AzureFirewallThreatIntelMode** |  |  [optional] |
|**virtualHub** | [**AzureFirewallIPConfigurationPropertiesFormatPublicIPAddress**](AzureFirewallIPConfigurationPropertiesFormatPublicIPAddress.md) |  |  [optional] |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| SUCCEEDED | &quot;Succeeded&quot; |
| UPDATING | &quot;Updating&quot; |
| DELETING | &quot;Deleting&quot; |
| FAILED | &quot;Failed&quot; |



