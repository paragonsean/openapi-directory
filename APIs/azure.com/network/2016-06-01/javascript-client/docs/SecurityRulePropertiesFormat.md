# NetworkManagementClient.SecurityRulePropertiesFormat

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access** | **String** | Gets or sets network traffic is allowed or denied. Possible values are &#39;Allow&#39; and &#39;Deny&#39; | 
**description** | **String** | Gets or sets a description for this rule. Restricted to 140 chars. | [optional] 
**destinationAddressPrefix** | **String** | Gets or sets destination address prefix. CIDR or source IP range. Asterisk &#39;*&#39; can also be used to match all source IPs. Default tags such as &#39;VirtualNetwork&#39;, &#39;AzureLoadBalancer&#39; and &#39;Internet&#39; can also be used.  | 
**destinationPortRange** | **String** | Gets or sets Destination Port or Range. Integer or range between 0 and 65535. Asterisk &#39;*&#39; can also be used to match all ports. | [optional] 
**direction** | **String** | Gets or sets the direction of the rule.InBound or Outbound. The direction specifies if rule will be evaluated on incoming or outgoing traffic. | 
**priority** | **Number** | Gets or sets the priority of the rule. The value can be between 100 and 4096. The priority number must be unique for each rule in the collection. The lower the priority number, the higher the priority of the rule. | [optional] 
**protocol** | **String** | Gets or sets Network protocol this rule applies to. Can be Tcp, Udp or All(*). | 
**provisioningState** | **String** | Gets provisioning state of the PublicIP resource Updating/Deleting/Failed | [optional] 
**sourceAddressPrefix** | **String** | Gets or sets source address prefix. CIDR or source IP range. Asterisk &#39;*&#39; can also be used to match all source IPs. Default tags such as &#39;VirtualNetwork&#39;, &#39;AzureLoadBalancer&#39; and &#39;Internet&#39; can also be used. If this is an ingress rule, specifies where network traffic originates from.  | 
**sourcePortRange** | **String** | Gets or sets Source Port or Range. Integer or range between 0 and 65535. Asterisk &#39;*&#39; can also be used to match all ports. | [optional] 



## Enum: AccessEnum


* `Allow` (value: `"Allow"`)

* `Deny` (value: `"Deny"`)





## Enum: DirectionEnum


* `Inbound` (value: `"Inbound"`)

* `Outbound` (value: `"Outbound"`)





## Enum: ProtocolEnum


* `Tcp` (value: `"Tcp"`)

* `Udp` (value: `"Udp"`)

* `STAR` (value: `"*"`)




