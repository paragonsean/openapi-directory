# NetworkManagementClient.ApplicationGatewayRedirectConfigurationPropertiesFormat

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**includePath** | **Boolean** | Include path in the redirected url. | [optional] 
**includeQueryString** | **Boolean** | Include query string in the redirected url. | [optional] 
**pathRules** | [**[ApplicationGatewayPathRulePropertiesFormatRewriteRuleSet]**](ApplicationGatewayPathRulePropertiesFormatRewriteRuleSet.md) | Path rules specifying redirect configuration. | [optional] 
**redirectType** | [**RedirectTypeEnum**](RedirectTypeEnum.md) |  | [optional] 
**requestRoutingRules** | [**[ApplicationGatewayPathRulePropertiesFormatRewriteRuleSet]**](ApplicationGatewayPathRulePropertiesFormatRewriteRuleSet.md) | Request routing specifying redirect configuration. | [optional] 
**targetListener** | [**ApplicationGatewayPathRulePropertiesFormatRewriteRuleSet**](ApplicationGatewayPathRulePropertiesFormatRewriteRuleSet.md) |  | [optional] 
**targetUrl** | **String** | Url to redirect the request to. | [optional] 
**urlPathMaps** | [**[ApplicationGatewayPathRulePropertiesFormatRewriteRuleSet]**](ApplicationGatewayPathRulePropertiesFormatRewriteRuleSet.md) | Url path maps specifying default redirect configuration. | [optional] 


