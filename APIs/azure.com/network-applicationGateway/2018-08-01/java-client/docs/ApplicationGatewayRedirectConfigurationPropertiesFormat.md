

# ApplicationGatewayRedirectConfigurationPropertiesFormat

Properties of redirect configuration of the application gateway.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**includePath** | **Boolean** | Include path in the redirected url. |  [optional] |
|**includeQueryString** | **Boolean** | Include query string in the redirected url. |  [optional] |
|**pathRules** | [**List&lt;ApplicationGatewayPathRulePropertiesFormatRedirectConfiguration&gt;**](ApplicationGatewayPathRulePropertiesFormatRedirectConfiguration.md) | Path rules specifying redirect configuration. |  [optional] |
|**redirectType** | **RedirectTypeEnum** |  |  [optional] |
|**requestRoutingRules** | [**List&lt;ApplicationGatewayPathRulePropertiesFormatRedirectConfiguration&gt;**](ApplicationGatewayPathRulePropertiesFormatRedirectConfiguration.md) | Request routing specifying redirect configuration. |  [optional] |
|**targetListener** | [**ApplicationGatewayPathRulePropertiesFormatRedirectConfiguration**](ApplicationGatewayPathRulePropertiesFormatRedirectConfiguration.md) |  |  [optional] |
|**targetUrl** | **String** | Url to redirect the request to. |  [optional] |
|**urlPathMaps** | [**List&lt;ApplicationGatewayPathRulePropertiesFormatRedirectConfiguration&gt;**](ApplicationGatewayPathRulePropertiesFormatRedirectConfiguration.md) | Url path maps specifying default redirect configuration. |  [optional] |



