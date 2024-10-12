# NetworkManagementClient.NetworkInterfaceAssociationSecurityRulesInnerProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access** | **String** | Whether network traffic is allowed or denied. | 
**description** | **String** | A description for this rule. Restricted to 140 chars. | [optional] 
**destinationAddressPrefix** | **String** | The destination address prefix. CIDR or destination IP range. Asterisk &#39;*&#39; can also be used to match all source IPs. Default tags such as &#39;VirtualNetwork&#39;, &#39;AzureLoadBalancer&#39; and &#39;Internet&#39; can also be used. | [optional] 
**destinationAddressPrefixes** | **[String]** | The destination address prefixes. CIDR or destination IP ranges. | [optional] 
**destinationApplicationSecurityGroups** | [**[NetworkInterfaceAssociationSecurityRulesInnerPropertiesDestinationApplicationSecurityGroupsInner]**](NetworkInterfaceAssociationSecurityRulesInnerPropertiesDestinationApplicationSecurityGroupsInner.md) | The application security group specified as destination. | [optional] 
**destinationPortRange** | **String** | The destination port or range. Integer or range between 0 and 65535. Asterisk &#39;*&#39; can also be used to match all ports. | [optional] 
**destinationPortRanges** | **[String]** | The destination port ranges. | [optional] 
**direction** | **String** | The direction of the rule. The direction specifies if rule will be evaluated on incoming or outgoing traffic. | 
**priority** | **Number** | The priority of the rule. The value can be between 100 and 4096. The priority number must be unique for each rule in the collection. The lower the priority number, the higher the priority of the rule. | [optional] 
**protocol** | **String** | Network protocol this rule applies to. | 
**provisioningState** | **String** | The provisioning state of the public IP resource. Possible values are: &#39;Updating&#39;, &#39;Deleting&#39;, and &#39;Failed&#39;. | [optional] 
**sourceAddressPrefix** | **String** | The CIDR or source IP range. Asterisk &#39;*&#39; can also be used to match all source IPs. Default tags such as &#39;VirtualNetwork&#39;, &#39;AzureLoadBalancer&#39; and &#39;Internet&#39; can also be used. If this is an ingress rule, specifies where network traffic originates from. | [optional] 
**sourceAddressPrefixes** | **[String]** | The CIDR or source IP ranges. | [optional] 
**sourceApplicationSecurityGroups** | [**[NetworkInterfaceAssociationSecurityRulesInnerPropertiesDestinationApplicationSecurityGroupsInner]**](NetworkInterfaceAssociationSecurityRulesInnerPropertiesDestinationApplicationSecurityGroupsInner.md) | The application security group specified as source. | [optional] 
**sourcePortRange** | **String** | The source port or range. Integer or range between 0 and 65535. Asterisk &#39;*&#39; can also be used to match all ports. | [optional] 
**sourcePortRanges** | **[String]** | The source port ranges. | [optional] 



## Enum: AccessEnum


* `Allow` (value: `"Allow"`)

* `Deny` (value: `"Deny"`)





## Enum: DirectionEnum


* `Inbound` (value: `"Inbound"`)

* `Outbound` (value: `"Outbound"`)





## Enum: ProtocolEnum


* `Tcp` (value: `"Tcp"`)

* `Udp` (value: `"Udp"`)

* `Icmp` (value: `"Icmp"`)

* `Esp` (value: `"Esp"`)

* `STAR` (value: `"*"`)




