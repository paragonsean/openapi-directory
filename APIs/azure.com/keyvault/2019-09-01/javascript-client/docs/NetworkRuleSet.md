# KeyVaultManagementClient.NetworkRuleSet

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bypass** | **String** | Tells what traffic can bypass network rules. This can be &#39;AzureServices&#39; or &#39;None&#39;.  If not specified the default is &#39;AzureServices&#39;. | [optional] 
**defaultAction** | **String** | The default action when no rule from ipRules and from virtualNetworkRules match. This is only used after the bypass property has been evaluated. | [optional] 
**ipRules** | [**[IPRule]**](IPRule.md) | The list of IP address rules. | [optional] 
**virtualNetworkRules** | [**[VirtualNetworkRule]**](VirtualNetworkRule.md) | The list of virtual network rules. | [optional] 



## Enum: BypassEnum


* `AzureServices` (value: `"AzureServices"`)

* `None` (value: `"None"`)





## Enum: DefaultActionEnum


* `Allow` (value: `"Allow"`)

* `Deny` (value: `"Deny"`)




