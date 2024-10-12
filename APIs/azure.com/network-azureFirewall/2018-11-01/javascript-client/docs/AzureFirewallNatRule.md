# NetworkManagementClient.AzureFirewallNatRule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **String** | Description of the rule. | [optional] 
**destinationAddresses** | **[String]** | List of destination IP addresses for this rule. | [optional] 
**destinationPorts** | **[String]** | List of destination ports. | [optional] 
**name** | **String** | Name of the NAT rule. | [optional] 
**protocols** | [**[AzureFirewallNetworkRuleProtocol]**](AzureFirewallNetworkRuleProtocol.md) | Array of AzureFirewallNetworkRuleProtocols applicable to this NAT rule. | [optional] 
**sourceAddresses** | **[String]** | List of source IP addresses for this rule. | [optional] 
**translatedAddress** | **String** | The translated address for this NAT rule. | [optional] 
**translatedPort** | **String** | The translated port for this NAT rule. | [optional] 


