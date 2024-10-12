

# NetworkRuleSet

A set of rules governing the network accessibility of a vault.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bypass** | [**BypassEnum**](#BypassEnum) | Tells what traffic can bypass network rules. This can be &#39;AzureServices&#39; or &#39;None&#39;.  If not specified the default is &#39;AzureServices&#39;. |  [optional] |
|**defaultAction** | [**DefaultActionEnum**](#DefaultActionEnum) | The default action when no rule from ipRules and from virtualNetworkRules match. This is only used after the bypass property has been evaluated. |  [optional] |
|**ipRules** | [**List&lt;IPRule&gt;**](IPRule.md) | The list of IP address rules. |  [optional] |
|**virtualNetworkRules** | [**List&lt;VirtualNetworkRule&gt;**](VirtualNetworkRule.md) | The list of virtual network rules. |  [optional] |



## Enum: BypassEnum

| Name | Value |
|---- | -----|
| AZURE_SERVICES | &quot;AzureServices&quot; |
| NONE | &quot;None&quot; |



## Enum: DefaultActionEnum

| Name | Value |
|---- | -----|
| ALLOW | &quot;Allow&quot; |
| DENY | &quot;Deny&quot; |



