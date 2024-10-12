

# NetworkRuleSet

Network rule set

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bypass** | [**BypassEnum**](#BypassEnum) | Specifies whether traffic is bypassed for Logging/Metrics/AzureServices. Possible values are any combination of Logging|Metrics|AzureServices (For example, \&quot;Logging, Metrics\&quot;), or None to bypass none of those traffics. |  [optional] |
|**defaultAction** | [**DefaultActionEnum**](#DefaultActionEnum) | Specifies the default action of allow or deny when no other rules match. |  |
|**ipRules** | [**List&lt;IPRule&gt;**](IPRule.md) | Sets the IP ACL rules |  [optional] |
|**virtualNetworkRules** | [**List&lt;VirtualNetworkRule&gt;**](VirtualNetworkRule.md) | Sets the virtual network rules |  [optional] |



## Enum: BypassEnum

| Name | Value |
|---- | -----|
| NONE | &quot;None&quot; |
| LOGGING | &quot;Logging&quot; |
| METRICS | &quot;Metrics&quot; |
| AZURE_SERVICES | &quot;AzureServices&quot; |



## Enum: DefaultActionEnum

| Name | Value |
|---- | -----|
| ALLOW | &quot;Allow&quot; |
| DENY | &quot;Deny&quot; |



