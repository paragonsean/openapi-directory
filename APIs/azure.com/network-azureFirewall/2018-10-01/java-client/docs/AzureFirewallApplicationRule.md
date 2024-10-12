

# AzureFirewallApplicationRule

Properties of an application rule.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | Description of the rule. |  [optional] |
|**fqdnTags** | **List&lt;String&gt;** | List of FQDN Tags for this rule. |  [optional] |
|**name** | **String** | Name of the application rule. |  [optional] |
|**protocols** | [**List&lt;AzureFirewallApplicationRuleProtocol&gt;**](AzureFirewallApplicationRuleProtocol.md) | Array of ApplicationRuleProtocols. |  [optional] |
|**sourceAddresses** | **List&lt;String&gt;** | List of source IP addresses for this rule. |  [optional] |
|**targetFqdns** | **List&lt;String&gt;** | List of FQDNs for this rule. |  [optional] |



