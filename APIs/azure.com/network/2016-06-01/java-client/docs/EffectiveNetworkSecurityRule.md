

# EffectiveNetworkSecurityRule

Effective NetworkSecurityRules

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**access** | [**AccessEnum**](#AccessEnum) | Gets network traffic is allowed or denied |  [optional] |
|**destinationAddressPrefix** | **String** | Gets destination address prefix |  [optional] |
|**destinationPortRange** | **String** | Gets destination port or range |  [optional] |
|**direction** | [**DirectionEnum**](#DirectionEnum) | Gets the direction of the rule |  [optional] |
|**expandedDestinationAddressPrefix** | **List&lt;String&gt;** | Gets expanded destination address prefix |  [optional] |
|**expandedSourceAddressPrefix** | **List&lt;String&gt;** | Gets expanded source address prefix |  [optional] |
|**name** | **String** | Gets the name of the security rule specified by the user (if created by the user) |  [optional] |
|**priority** | **Integer** | Gets the priority of the rule |  [optional] |
|**protocol** | [**ProtocolEnum**](#ProtocolEnum) | Gets Network protocol this rule applies to |  [optional] |
|**sourceAddressPrefix** | **String** | Gets source address prefix |  [optional] |
|**sourcePortRange** | **String** | Gets source port or range |  [optional] |



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



