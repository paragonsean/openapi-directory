

# CreateApplicationRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**apiGatewayProxy** | [**CreateApplicationRequestApiGatewayProxy**](CreateApplicationRequestApiGatewayProxy.md) |  |  [optional] |
|**clientToken** | **String** | A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. |  [optional] |
|**name** | **String** | The name to use for the application.  |  |
|**proxyType** | [**ProxyTypeEnum**](#ProxyTypeEnum) | The proxy type of the proxy created within the application.  |  |
|**tags** | **Map&lt;String, String&gt;** | A collection of up to 50 unique tags |  [optional] |
|**vpcId** | **String** | The ID of the virtual private cloud (VPC). |  |



## Enum: ProxyTypeEnum

| Name | Value |
|---- | -----|
| API_GATEWAY | &quot;API_GATEWAY&quot; |



