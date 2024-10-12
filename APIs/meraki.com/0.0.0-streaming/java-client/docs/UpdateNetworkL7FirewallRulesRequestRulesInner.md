

# UpdateNetworkL7FirewallRulesRequestRulesInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**policy** | [**PolicyEnum**](#PolicyEnum) | &#39;Deny&#39; traffic specified by this rule |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Type of the L7 rule. One of: &#39;application&#39;, &#39;applicationCategory&#39;, &#39;host&#39;, &#39;port&#39;, &#39;ipRange&#39; |  [optional] |
|**value** | **String** | The &#39;value&#39; of what you want to block. Format of &#39;value&#39; varies depending on type of the rule. The application categories and application ids can be retrieved from the the &#39;MX L7 application categories&#39; endpoint. The countries follow the two-letter ISO 3166-1 alpha-2 format. |  [optional] |



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



