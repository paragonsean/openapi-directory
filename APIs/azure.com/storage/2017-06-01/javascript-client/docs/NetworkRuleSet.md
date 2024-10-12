# StorageManagement.NetworkRuleSet

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bypass** | **String** | Specifies whether traffic is bypassed for Logging/Metrics/AzureServices. Possible values are any combination of Logging|Metrics|AzureServices (For example, \&quot;Logging, Metrics\&quot;), or None to bypass none of those traffics. | [optional] [default to &#39;AzureServices&#39;]
**defaultAction** | **String** | Specifies the default action of allow or deny when no other rules match. | [default to &#39;Allow&#39;]
**ipRules** | [**[IPRule]**](IPRule.md) | Sets the IP ACL rules | [optional] 
**virtualNetworkRules** | [**[VirtualNetworkRule]**](VirtualNetworkRule.md) | Sets the virtual network rules | [optional] 



## Enum: BypassEnum


* `None` (value: `"None"`)

* `Logging` (value: `"Logging"`)

* `Metrics` (value: `"Metrics"`)

* `AzureServices` (value: `"AzureServices"`)





## Enum: DefaultActionEnum


* `Allow` (value: `"Allow"`)

* `Deny` (value: `"Deny"`)




