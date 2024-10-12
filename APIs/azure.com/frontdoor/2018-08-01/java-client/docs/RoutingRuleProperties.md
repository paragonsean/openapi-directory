

# RoutingRuleProperties

The JSON object that contains the properties required to create a routing rule.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**resourceState** | **ResourceState** |  |  [optional] |
|**acceptedProtocols** | [**List&lt;AcceptedProtocolsEnum&gt;**](#List&lt;AcceptedProtocolsEnum&gt;) | Protocol schemes to match for this rule |  [optional] |
|**backendPool** | [**BackendPoolUpdateParametersHealthProbeSettings**](BackendPoolUpdateParametersHealthProbeSettings.md) |  |  [optional] |
|**cacheConfiguration** | [**CacheConfiguration**](CacheConfiguration.md) |  |  [optional] |
|**customForwardingPath** | **String** | A custom path used to rewrite resource paths matched by this rule. Leave empty to use incoming path. |  [optional] |
|**enabledState** | [**EnabledStateEnum**](#EnabledStateEnum) | Whether to enable use of this rule. Permitted values are &#39;Enabled&#39; or &#39;Disabled&#39; |  [optional] |
|**forwardingProtocol** | [**ForwardingProtocolEnum**](#ForwardingProtocolEnum) | Protocol this rule will use when forwarding traffic to backends. |  [optional] |
|**frontendEndpoints** | [**List&lt;BackendPoolUpdateParametersHealthProbeSettings&gt;**](BackendPoolUpdateParametersHealthProbeSettings.md) | Frontend endpoints associated with this rule |  [optional] |
|**patternsToMatch** | **List&lt;String&gt;** | The route patterns of the rule. |  [optional] |



## Enum: List&lt;AcceptedProtocolsEnum&gt;

| Name | Value |
|---- | -----|
| HTTP | &quot;Http&quot; |
| HTTPS | &quot;Https&quot; |



## Enum: EnabledStateEnum

| Name | Value |
|---- | -----|
| ENABLED | &quot;Enabled&quot; |
| DISABLED | &quot;Disabled&quot; |



## Enum: ForwardingProtocolEnum

| Name | Value |
|---- | -----|
| HTTP_ONLY | &quot;HttpOnly&quot; |
| HTTPS_ONLY | &quot;HttpsOnly&quot; |
| MATCH_REQUEST | &quot;MatchRequest&quot; |



