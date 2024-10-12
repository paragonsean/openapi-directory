# FrontDoorManagementClient.RoutingRuleProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resourceState** | [**ResourceState**](ResourceState.md) |  | [optional] 
**acceptedProtocols** | **[String]** | Protocol schemes to match for this rule | [optional] 
**backendPool** | [**BackendPoolUpdateParametersHealthProbeSettings**](BackendPoolUpdateParametersHealthProbeSettings.md) |  | [optional] 
**cacheConfiguration** | [**CacheConfiguration**](CacheConfiguration.md) |  | [optional] 
**customForwardingPath** | **String** | A custom path used to rewrite resource paths matched by this rule. Leave empty to use incoming path. | [optional] 
**enabledState** | **String** | Whether to enable use of this rule. Permitted values are &#39;Enabled&#39; or &#39;Disabled&#39; | [optional] 
**forwardingProtocol** | **String** | Protocol this rule will use when forwarding traffic to backends. | [optional] 
**frontendEndpoints** | [**[BackendPoolUpdateParametersHealthProbeSettings]**](BackendPoolUpdateParametersHealthProbeSettings.md) | Frontend endpoints associated with this rule | [optional] 
**patternsToMatch** | **[String]** | The route patterns of the rule. | [optional] 



## Enum: [AcceptedProtocolsEnum]


* `Http` (value: `"Http"`)

* `Https` (value: `"Https"`)





## Enum: EnabledStateEnum


* `Enabled` (value: `"Enabled"`)

* `Disabled` (value: `"Disabled"`)





## Enum: ForwardingProtocolEnum


* `HttpOnly` (value: `"HttpOnly"`)

* `HttpsOnly` (value: `"HttpsOnly"`)

* `MatchRequest` (value: `"MatchRequest"`)




