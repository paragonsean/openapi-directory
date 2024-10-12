

# ApplicationGatewayRedirectConfigurationPropertiesFormat

Properties of redirect configuration of the application gateway.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**includePath** | **Boolean** | Include path in the redirected url. |  [optional] |
|**includeQueryString** | **Boolean** | Include query string in the redirected url. |  [optional] |
|**pathRules** | **List&lt;Model0&gt;** | Path rules specifying redirect configuration. |  [optional] |
|**redirectType** | **RedirectTypeEnum** |  |  [optional] |
|**requestRoutingRules** | **List&lt;Model0&gt;** | Request routing specifying redirect configuration. |  [optional] |
|**targetListener** | **Model0** |  |  [optional] |
|**targetUrl** | **String** | Url to redirect the request to. |  [optional] |
|**urlPathMaps** | **List&lt;Model0&gt;** | Url path maps specifying default redirect configuration. |  [optional] |



