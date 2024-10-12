# NetworkManagementClient.SecurityRuleAssociationsEffectiveSecurityRulesInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access** | **String** | Whether network traffic is allowed or denied. Possible values are: &#39;Allow&#39; and &#39;Deny&#39;. | [optional] 
**destinationAddressPrefix** | **String** | The destination address prefix. | [optional] 
**destinationAddressPrefixes** | **[String]** | The destination address prefixes. Expected values include CIDR IP ranges, Default Tags (VirtualNetwork, AzureLoadBalancer, Internet), System Tags, and the asterisk (*). | [optional] 
**destinationPortRange** | **String** | The destination port or range. | [optional] 
**destinationPortRanges** | **[String]** | The destination port ranges. Expected values include a single integer between 0 and 65535, a range using &#39;-&#39; as separator (e.g. 100-400), or an asterisk (*) | [optional] 
**direction** | **String** | The direction of the rule. Possible values are: &#39;Inbound and Outbound&#39;. | [optional] 
**expandedDestinationAddressPrefix** | **[String]** | Expanded destination address prefix. | [optional] 
**expandedSourceAddressPrefix** | **[String]** | The expanded source address prefix. | [optional] 
**name** | **String** | The name of the security rule specified by the user (if created by the user). | [optional] 
**priority** | **Number** | The priority of the rule. | [optional] 
**protocol** | **String** | The network protocol this rule applies to. Possible values are: &#39;Tcp&#39;, &#39;Udp&#39;, and &#39;All&#39;. | [optional] 
**sourceAddressPrefix** | **String** | The source address prefix. | [optional] 
**sourceAddressPrefixes** | **[String]** | The source address prefixes. Expected values include CIDR IP ranges, Default Tags (VirtualNetwork, AzureLoadBalancer, Internet), System Tags, and the asterisk (*). | [optional] 
**sourcePortRange** | **String** | The source port or range. | [optional] 
**sourcePortRanges** | **[String]** | The source port ranges. Expected values include a single integer between 0 and 65535, a range using &#39;-&#39; as separator (e.g. 100-400), or an asterisk (*) | [optional] 



## Enum: AccessEnum


* `Allow` (value: `"Allow"`)

* `Deny` (value: `"Deny"`)





## Enum: DirectionEnum


* `Inbound` (value: `"Inbound"`)

* `Outbound` (value: `"Outbound"`)





## Enum: ProtocolEnum


* `Tcp` (value: `"Tcp"`)

* `Udp` (value: `"Udp"`)

* `All` (value: `"All"`)




