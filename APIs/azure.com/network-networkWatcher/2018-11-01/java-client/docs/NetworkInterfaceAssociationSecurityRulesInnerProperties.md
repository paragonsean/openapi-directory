

# NetworkInterfaceAssociationSecurityRulesInnerProperties

Security rule resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**access** | [**AccessEnum**](#AccessEnum) | The network traffic is allowed or denied. Possible values are: &#39;Allow&#39; and &#39;Deny&#39;. |  |
|**description** | **String** | A description for this rule. Restricted to 140 chars. |  [optional] |
|**destinationAddressPrefix** | **String** | The destination address prefix. CIDR or destination IP range. Asterisks &#39;*&#39; can also be used to match all source IPs. Default tags such as &#39;VirtualNetwork&#39;, &#39;AzureLoadBalancer&#39; and &#39;Internet&#39; can also be used. |  [optional] |
|**destinationAddressPrefixes** | **List&lt;String&gt;** | The destination address prefixes. CIDR or destination IP ranges. |  [optional] |
|**destinationApplicationSecurityGroups** | [**List&lt;NetworkInterfaceAssociationSecurityRulesInnerPropertiesDestinationApplicationSecurityGroupsInner&gt;**](NetworkInterfaceAssociationSecurityRulesInnerPropertiesDestinationApplicationSecurityGroupsInner.md) | The application security group specified as destination. |  [optional] |
|**destinationPortRange** | **String** | The destination port or range. Integer or range between 0 and 65535. Asterisks &#39;*&#39; can also be used to match all ports. |  [optional] |
|**destinationPortRanges** | **List&lt;String&gt;** | The destination port ranges. |  [optional] |
|**direction** | [**DirectionEnum**](#DirectionEnum) | The direction of the rule. The direction specifies if rule will be evaluated on incoming or outgoing traffic. Possible values are: &#39;Inbound&#39; and &#39;Outbound&#39;. |  |
|**priority** | **Integer** | The priority of the rule. The value can be between 100 and 4096. The priority number must be unique for each rule in the collection. The lower the priority number, the higher the priority of the rule. |  [optional] |
|**protocol** | [**ProtocolEnum**](#ProtocolEnum) | Network protocol this rule applies to. Possible values are &#39;Tcp&#39;, &#39;Udp&#39;, and &#39;*&#39;. |  |
|**provisioningState** | **String** | The provisioning state of the public IP resource. Possible values are: &#39;Updating&#39;, &#39;Deleting&#39;, and &#39;Failed&#39;. |  [optional] |
|**sourceAddressPrefix** | **String** | The CIDR or source IP range. Asterisks &#39;*&#39; can also be used to match all source IPs. Default tags such as &#39;VirtualNetwork&#39;, &#39;AzureLoadBalancer&#39; and &#39;Internet&#39; can also be used. If this is an ingress rule, specifies where network traffic originates from.  |  [optional] |
|**sourceAddressPrefixes** | **List&lt;String&gt;** | The CIDR or source IP ranges. |  [optional] |
|**sourceApplicationSecurityGroups** | [**List&lt;NetworkInterfaceAssociationSecurityRulesInnerPropertiesDestinationApplicationSecurityGroupsInner&gt;**](NetworkInterfaceAssociationSecurityRulesInnerPropertiesDestinationApplicationSecurityGroupsInner.md) | The application security group specified as source. |  [optional] |
|**sourcePortRange** | **String** | The source port or range. Integer or range between 0 and 65535. Asterisks &#39;*&#39; can also be used to match all ports. |  [optional] |
|**sourcePortRanges** | **List&lt;String&gt;** | The source port ranges. |  [optional] |



## Enum: AccessEnum

| Name | Value |
|---- | -----|
| ALLOW | &quot;Allow&quot; |
| DENY | &quot;Deny&quot; |



## Enum: DirectionEnum

| Name | Value |
|---- | -----|
| INBOUND | &quot;Inbound&quot; |
| OUTBOUND | &quot;Outbound&quot; |



## Enum: ProtocolEnum

| Name | Value |
|---- | -----|
| TCP | &quot;Tcp&quot; |
| UDP | &quot;Udp&quot; |
| STAR | &quot;*&quot; |



