

# ApplicationGatewayUrlPathMapPropertiesFormat

Properties of UrlPathMap of the application gateway.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**defaultBackendAddressPool** | **Model0** |  |  [optional] |
|**defaultBackendHttpSettings** | **Model0** |  |  [optional] |
|**defaultRedirectConfiguration** | **Model0** |  |  [optional] |
|**defaultRewriteRuleSet** | **Model0** |  |  [optional] |
|**pathRules** | [**List&lt;ApplicationGatewayPathRule&gt;**](ApplicationGatewayPathRule.md) | Path rule of URL path map resource. |  [optional] |
|**provisioningState** | **String** | Provisioning state of the backend http settings resource. Possible values are: &#39;Updating&#39;, &#39;Deleting&#39;, and &#39;Failed&#39;. |  [optional] |



