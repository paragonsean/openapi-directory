

# ApplicationGatewayUrlPathMapPropertiesFormat

Properties of UrlPathMap of application gateway

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**defaultBackendAddressPool** | [**SubResource**](SubResource.md) |  |  [optional] |
|**defaultBackendHttpSettings** | [**SubResource**](SubResource.md) |  |  [optional] |
|**pathRules** | [**List&lt;ApplicationGatewayPathRule&gt;**](ApplicationGatewayPathRule.md) | Path rule of URL path map resource |  [optional] |
|**provisioningState** | **String** | Provisioning state of the backend http settings resource Updating/Deleting/Failed |  [optional] |



