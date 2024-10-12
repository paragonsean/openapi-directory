# NetworkManagementClient.ApplicationGatewayRedirectConfigurationPropertiesFormat

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**includePath** | **Boolean** | Include path in the redirected url. | [optional] 
**includeQueryString** | **Boolean** | Include query string in the redirected url. | [optional] 
**pathRules** | [**[ApplicationGatewayPathRulePropertiesFormatRedirectConfiguration]**](ApplicationGatewayPathRulePropertiesFormatRedirectConfiguration.md) | Path rules specifying redirect configuration. | [optional] 
**redirectType** | [**RedirectTypeEnum**](RedirectTypeEnum.md) |  | [optional] 
**requestRoutingRules** | [**[ApplicationGatewayPathRulePropertiesFormatRedirectConfiguration]**](ApplicationGatewayPathRulePropertiesFormatRedirectConfiguration.md) | Request routing specifying redirect configuration. | [optional] 
**targetListener** | [**ApplicationGatewayPathRulePropertiesFormatRedirectConfiguration**](ApplicationGatewayPathRulePropertiesFormatRedirectConfiguration.md) |  | [optional] 
**targetUrl** | **String** | Url to redirect the request to. | [optional] 
**urlPathMaps** | [**[ApplicationGatewayPathRulePropertiesFormatRedirectConfiguration]**](ApplicationGatewayPathRulePropertiesFormatRedirectConfiguration.md) | Url path maps specifying default redirect configuration. | [optional] 


