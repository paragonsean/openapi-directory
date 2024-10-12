

# SecurityRuleAssociationsEffectiveSecurityRulesInner

Effective network security rules.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**access** | [**AccessEnum**](#AccessEnum) | Whether network traffic is allowed or denied. Possible values are: &#39;Allow&#39; and &#39;Deny&#39;. |  [optional] |
|**destinationAddressPrefix** | **String** | The destination address prefix. |  [optional] |
|**destinationPortRange** | **String** | The destination port or range. |  [optional] |
|**direction** | [**DirectionEnum**](#DirectionEnum) | The direction of the rule. Possible values are: &#39;Inbound and Outbound&#39;. |  [optional] |
|**expandedDestinationAddressPrefix** | **List&lt;String&gt;** | Expanded destination address prefix. |  [optional] |
|**expandedSourceAddressPrefix** | **List&lt;String&gt;** | The expanded source address prefix. |  [optional] |
|**name** | **String** | The name of the security rule specified by the user (if created by the user). |  [optional] |
|**priority** | **Integer** | The priority of the rule. |  [optional] |
|**protocol** | [**ProtocolEnum**](#ProtocolEnum) | The network protocol this rule applies to. Possible values are: &#39;Tcp&#39;, &#39;Udp&#39;, and &#39;*&#39;. |  [optional] |
|**sourceAddressPrefix** | **String** | The source address prefix. |  [optional] |
|**sourcePortRange** | **String** | The source port or range. |  [optional] |



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



