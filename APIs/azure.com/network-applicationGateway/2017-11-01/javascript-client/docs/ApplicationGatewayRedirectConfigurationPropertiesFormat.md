# NetworkManagementClient.ApplicationGatewayRedirectConfigurationPropertiesFormat

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**includePath** | **Boolean** | Include path in the redirected url. | [optional] 
**includeQueryString** | **Boolean** | Include query string in the redirected url. | [optional] 
**pathRules** | [**[Model0]**](Model0.md) | Path rules specifying redirect configuration. | [optional] 
**redirectType** | [**RedirectTypeEnum**](RedirectTypeEnum.md) |  | [optional] 
**requestRoutingRules** | [**[Model0]**](Model0.md) | Request routing specifying redirect configuration. | [optional] 
**targetListener** | [**Model0**](Model0.md) |  | [optional] 
**targetUrl** | **String** | Url to redirect the request to. | [optional] 
**urlPathMaps** | [**[Model0]**](Model0.md) | Url path maps specifying default redirect configuration. | [optional] 


