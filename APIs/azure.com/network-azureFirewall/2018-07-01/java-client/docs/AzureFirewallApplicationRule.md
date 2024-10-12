

# AzureFirewallApplicationRule

Properties of an application rule.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | Description of the rule. |  [optional] |
|**name** | **String** | Name of the application rule. |  [optional] |
|**protocols** | [**List&lt;AzureFirewallApplicationRuleProtocol&gt;**](AzureFirewallApplicationRuleProtocol.md) | Array of ApplicationRuleProtocols. |  [optional] |
|**sourceAddresses** | **List&lt;String&gt;** | List of source IP addresses for this rule. |  [optional] |
|**targetUrls** | **List&lt;String&gt;** | List of URLs for this rule. |  [optional] |



