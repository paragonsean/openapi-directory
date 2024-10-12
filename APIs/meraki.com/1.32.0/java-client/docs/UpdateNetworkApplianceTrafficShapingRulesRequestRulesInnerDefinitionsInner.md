

# UpdateNetworkApplianceTrafficShapingRulesRequestRulesInnerDefinitionsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**type** | [**TypeEnum**](#TypeEnum) | The type of definition. Can be one of &#39;application&#39;, &#39;applicationCategory&#39;, &#39;host&#39;, &#39;port&#39;, &#39;ipRange&#39; or &#39;localNet&#39;. |  |
|**value** | **String** |     If \&quot;type\&quot; is &#39;host&#39;, &#39;port&#39;, &#39;ipRange&#39; or &#39;localNet&#39;, then \&quot;value\&quot; must be a string, matching either     a hostname (e.g. \&quot;somesite.com\&quot;), a port (e.g. 8080), or an IP range (\&quot;192.1.0.0\&quot;,     \&quot;192.1.0.0/16\&quot;, or \&quot;10.1.0.0/16:80\&quot;). &#39;localNet&#39; also supports CIDR notation, excluding     custom ports.      If \&quot;type\&quot; is &#39;application&#39; or &#39;applicationCategory&#39;, then \&quot;value\&quot; must be an object     with the structure { \&quot;id\&quot;: \&quot;meraki:layer7/...\&quot; }, where \&quot;id\&quot; is the application category or     application ID (for a list of IDs for your network, use the trafficShaping/applicationCategories     endpoint).  |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| APPLICATION | &quot;application&quot; |
| APPLICATION_CATEGORY | &quot;applicationCategory&quot; |
| HOST | &quot;host&quot; |
| IP_RANGE | &quot;ipRange&quot; |
| LOCAL_NET | &quot;localNet&quot; |
| PORT | &quot;port&quot; |



