# NetworkManagementClient.EffectiveNetworkSecurityRule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access** | **String** | Gets network traffic is allowed or denied | [optional] 
**destinationAddressPrefix** | **String** | Gets destination address prefix | [optional] 
**destinationPortRange** | **String** | Gets destination port or range | [optional] 
**direction** | **String** | Gets the direction of the rule | [optional] 
**expandedDestinationAddressPrefix** | **[String]** | Gets expanded destination address prefix | [optional] 
**expandedSourceAddressPrefix** | **[String]** | Gets expanded source address prefix | [optional] 
**name** | **String** | Gets the name of the security rule specified by the user (if created by the user) | [optional] 
**priority** | **Number** | Gets the priority of the rule | [optional] 
**protocol** | **String** | Gets Network protocol this rule applies to | [optional] 
**sourceAddressPrefix** | **String** | Gets source address prefix | [optional] 
**sourcePortRange** | **String** | Gets source port or range | [optional] 



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




