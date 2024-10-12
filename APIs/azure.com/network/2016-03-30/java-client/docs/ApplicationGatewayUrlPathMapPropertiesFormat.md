

# ApplicationGatewayUrlPathMapPropertiesFormat

Properties of probe of application gateway

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**defaultBackendAddressPool** | [**SubResource**](SubResource.md) |  |  [optional] |
|**defaultBackendHttpSettings** | [**SubResource**](SubResource.md) |  |  [optional] |
|**pathRules** | [**List&lt;ApplicationGatewayPathRule&gt;**](ApplicationGatewayPathRule.md) | Gets or sets path rule of URL path map resource |  [optional] |
|**provisioningState** | **String** | Gets or sets Provisioning state of the backend http settings resource Updating/Deleting/Failed |  [optional] |



