

# ApplicationGatewayRedirectConfigurationPropertiesFormat

Properties of redirect configuration of the application gateway.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**includePath** | **Boolean** | Include path in the redirected url. |  [optional] |
|**includeQueryString** | **Boolean** | Include query string in the redirected url. |  [optional] |
|**pathRules** | [**List&lt;ApplicationGatewayPathRulePropertiesFormatRewriteRuleSet&gt;**](ApplicationGatewayPathRulePropertiesFormatRewriteRuleSet.md) | Path rules specifying redirect configuration. |  [optional] |
|**redirectType** | **RedirectTypeEnum** |  |  [optional] |
|**requestRoutingRules** | [**List&lt;ApplicationGatewayPathRulePropertiesFormatRewriteRuleSet&gt;**](ApplicationGatewayPathRulePropertiesFormatRewriteRuleSet.md) | Request routing specifying redirect configuration. |  [optional] |
|**targetListener** | [**ApplicationGatewayPathRulePropertiesFormatRewriteRuleSet**](ApplicationGatewayPathRulePropertiesFormatRewriteRuleSet.md) |  |  [optional] |
|**targetUrl** | **String** | Url to redirect the request to. |  [optional] |
|**urlPathMaps** | [**List&lt;ApplicationGatewayPathRulePropertiesFormatRewriteRuleSet&gt;**](ApplicationGatewayPathRulePropertiesFormatRewriteRuleSet.md) | Url path maps specifying default redirect configuration. |  [optional] |



