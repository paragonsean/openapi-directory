

# UpdateNetworkWirelessSsidFirewallL7FirewallRulesRequestRulesInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**policy** | [**PolicyEnum**](#PolicyEnum) | &#39;Deny&#39; traffic specified by this rule |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Type of the L7 firewall rule. One of: &#39;application&#39;, &#39;applicationCategory&#39;, &#39;host&#39;, &#39;port&#39;, &#39;ipRange&#39; |  [optional] |
|**value** | **String** | The value of what needs to get blocked. Format of the value varies depending on type of the firewall rule selected. |  [optional] |



## Enum: PolicyEnum

| Name | Value |
|---- | -----|
| DENY | &quot;deny&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| APPLICATION | &quot;application&quot; |
| APPLICATION_CATEGORY | &quot;applicationCategory&quot; |
| HOST | &quot;host&quot; |
| IP_RANGE | &quot;ipRange&quot; |
| PORT | &quot;port&quot; |



