

# AzureFirewallNatRule

Properties of a NAT rule.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | Description of the rule. |  [optional] |
|**destinationAddresses** | **List&lt;String&gt;** | List of destination IP addresses for this rule. |  [optional] |
|**destinationPorts** | **List&lt;String&gt;** | List of destination ports. |  [optional] |
|**name** | **String** | Name of the NAT rule. |  [optional] |
|**protocols** | **List&lt;AzureFirewallNetworkRuleProtocol&gt;** | Array of AzureFirewallNetworkRuleProtocols applicable to this NAT rule. |  [optional] |
|**sourceAddresses** | **List&lt;String&gt;** | List of source IP addresses for this rule. |  [optional] |
|**translatedAddress** | **String** | The translated address for this NAT rule. |  [optional] |
|**translatedPort** | **String** | The translated port for this NAT rule. |  [optional] |



