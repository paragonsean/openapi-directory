# FrontDoorManagementClient.RoutingRuleUpdateParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acceptedProtocols** | **[String]** | Protocol schemes to match for this rule | [optional] 
**enabledState** | **String** | Whether to enable use of this rule. Permitted values are &#39;Enabled&#39; or &#39;Disabled&#39; | [optional] 
**frontendEndpoints** | [**[BackendPoolUpdateParametersHealthProbeSettings]**](BackendPoolUpdateParametersHealthProbeSettings.md) | Frontend endpoints associated with this rule | [optional] 
**patternsToMatch** | **[String]** | The route patterns of the rule. | [optional] 
**routeConfiguration** | [**RouteConfiguration**](RouteConfiguration.md) |  | [optional] 



## Enum: [AcceptedProtocolsEnum]


* `Http` (value: `"Http"`)

* `Https` (value: `"Https"`)





## Enum: EnabledStateEnum


* `Enabled` (value: `"Enabled"`)

* `Disabled` (value: `"Disabled"`)




