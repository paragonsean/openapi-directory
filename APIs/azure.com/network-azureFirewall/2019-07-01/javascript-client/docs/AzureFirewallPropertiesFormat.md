# NetworkManagementClient.AzureFirewallPropertiesFormat

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applicationRuleCollections** | [**[AzureFirewallApplicationRuleCollection]**](AzureFirewallApplicationRuleCollection.md) | Collection of application rule collections used by Azure Firewall. | [optional] 
**firewallPolicy** | [**AzureFirewallIPConfigurationPropertiesFormatPublicIPAddress**](AzureFirewallIPConfigurationPropertiesFormatPublicIPAddress.md) |  | [optional] 
**hubIpAddresses** | [**HubIPAddresses**](HubIPAddresses.md) |  | [optional] 
**ipConfigurations** | [**[AzureFirewallIPConfiguration]**](AzureFirewallIPConfiguration.md) | IP configuration of the Azure Firewall resource. | [optional] 
**natRuleCollections** | [**[AzureFirewallNatRuleCollection]**](AzureFirewallNatRuleCollection.md) | Collection of NAT rule collections used by Azure Firewall. | [optional] 
**networkRuleCollections** | [**[AzureFirewallNetworkRuleCollection]**](AzureFirewallNetworkRuleCollection.md) | Collection of network rule collections used by Azure Firewall. | [optional] 
**provisioningState** | **String** | The current provisioning state. | [optional] [readonly] 
**threatIntelMode** | [**AzureFirewallThreatIntelMode**](AzureFirewallThreatIntelMode.md) |  | [optional] 
**virtualHub** | [**AzureFirewallIPConfigurationPropertiesFormatPublicIPAddress**](AzureFirewallIPConfigurationPropertiesFormatPublicIPAddress.md) |  | [optional] 



## Enum: ProvisioningStateEnum


* `Succeeded` (value: `"Succeeded"`)

* `Updating` (value: `"Updating"`)

* `Deleting` (value: `"Deleting"`)

* `Failed` (value: `"Failed"`)




