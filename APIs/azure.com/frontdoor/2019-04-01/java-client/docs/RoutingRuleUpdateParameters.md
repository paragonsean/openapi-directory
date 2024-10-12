

# RoutingRuleUpdateParameters

Routing rules to apply to an endpoint

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**acceptedProtocols** | [**List&lt;AcceptedProtocolsEnum&gt;**](#List&lt;AcceptedProtocolsEnum&gt;) | Protocol schemes to match for this rule |  [optional] |
|**enabledState** | [**EnabledStateEnum**](#EnabledStateEnum) | Whether to enable use of this rule. Permitted values are &#39;Enabled&#39; or &#39;Disabled&#39; |  [optional] |
|**frontendEndpoints** | [**List&lt;BackendPoolUpdateParametersHealthProbeSettings&gt;**](BackendPoolUpdateParametersHealthProbeSettings.md) | Frontend endpoints associated with this rule |  [optional] |
|**patternsToMatch** | **List&lt;String&gt;** | The route patterns of the rule. |  [optional] |
|**routeConfiguration** | [**RouteConfiguration**](RouteConfiguration.md) |  |  [optional] |



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



