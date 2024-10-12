

# ApplicationRuleCondition

Rule condition of type application.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**destinationAddresses** | **List&lt;String&gt;** | List of destination IP addresses or Service Tags. |  [optional] |
|**fqdnTags** | **List&lt;String&gt;** | List of FQDN Tags for this rule condition. |  [optional] |
|**protocols** | [**List&lt;FirewallPolicyRuleConditionApplicationProtocol&gt;**](FirewallPolicyRuleConditionApplicationProtocol.md) | Array of Application Protocols. |  [optional] |
|**sourceAddresses** | **List&lt;String&gt;** | List of source IP addresses for this rule. |  [optional] |
|**targetFqdns** | **List&lt;String&gt;** | List of FQDNs for this rule condition. |  [optional] |



