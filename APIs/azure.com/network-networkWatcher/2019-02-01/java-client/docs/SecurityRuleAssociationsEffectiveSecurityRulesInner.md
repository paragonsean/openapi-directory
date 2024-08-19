

# SecurityRuleAssociationsEffectiveSecurityRulesInner

Effective network security rules.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**access** | [**AccessEnum**](#AccessEnum) | Whether network traffic is allowed or denied. |  [optional] |
|**destinationAddressPrefix** | **String** | The destination address prefix. |  [optional] |
|**destinationAddressPrefixes** | **List&lt;String&gt;** | The destination address prefixes. Expected values include CIDR IP ranges, Default Tags (VirtualNetwork, AzureLoadBalancer, Internet), System Tags, and the asterisk (*). |  [optional] |
|**destinationPortRange** | **String** | The destination port or range. |  [optional] |
|**destinationPortRanges** | **List&lt;String&gt;** | The destination port ranges. Expected values include a single integer between 0 and 65535, a range using &#39;-&#39; as separator (e.g. 100-400), or an asterisk (*) |  [optional] |
|**direction** | [**DirectionEnum**](#DirectionEnum) | The direction of the rule. The direction specifies if rule will be evaluated on incoming or outgoing traffic. |  [optional] |
|**expandedDestinationAddressPrefix** | **List&lt;String&gt;** | Expanded destination address prefix. |  [optional] |
|**expandedSourceAddressPrefix** | **List&lt;String&gt;** | The expanded source address prefix. |  [optional] |
|**name** | **String** | The name of the security rule specified by the user (if created by the user). |  [optional] |
|**priority** | **Integer** | The priority of the rule. |  [optional] |
|**protocol** | [**ProtocolEnum**](#ProtocolEnum) | The network protocol this rule applies to. Possible values are: &#39;Tcp&#39;, &#39;Udp&#39;, and &#39;All&#39;. |  [optional] |
|**sourceAddressPrefix** | **String** | The source address prefix. |  [optional] |
|**sourceAddressPrefixes** | **List&lt;String&gt;** | The source address prefixes. Expected values include CIDR IP ranges, Default Tags (VirtualNetwork, AzureLoadBalancer, Internet), System Tags, and the asterisk (*). |  [optional] |
|**sourcePortRange** | **String** | The source port or range. |  [optional] |
|**sourcePortRanges** | **List&lt;String&gt;** | The source port ranges. Expected values include a single integer between 0 and 65535, a range using &#39;-&#39; as separator (e.g. 100-400), or an asterisk (*) |  [optional] |



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
| ALL | &quot;All&quot; |



