

# ApplicationGatewayHttpListenerPropertiesFormat

Properties of HTTP listener of an application gateway.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**frontendIPConfiguration** | [**ApplicationGatewayHttpListenerPropertiesFormatFrontendPort**](ApplicationGatewayHttpListenerPropertiesFormatFrontendPort.md) |  |  [optional] |
|**frontendPort** | [**ApplicationGatewayHttpListenerPropertiesFormatFrontendPort**](ApplicationGatewayHttpListenerPropertiesFormatFrontendPort.md) |  |  [optional] |
|**hostName** | **String** | Host name of HTTP listener. |  [optional] |
|**protocol** | [**ProtocolEnum**](#ProtocolEnum) | Protocol. |  [optional] |
|**provisioningState** | **String** | Provisioning state of the HTTP listener resource. Possible values are: &#39;Updating&#39;, &#39;Deleting&#39;, and &#39;Failed&#39;. |  [optional] |
|**requireServerNameIndication** | **Boolean** | Applicable only if protocol is https. Enables SNI for multi-hosting. |  [optional] |
|**sslCertificate** | [**ApplicationGatewayHttpListenerPropertiesFormatFrontendPort**](ApplicationGatewayHttpListenerPropertiesFormatFrontendPort.md) |  |  [optional] |



## Enum: ProtocolEnum

| Name | Value |
|---- | -----|
| HTTP | &quot;Http&quot; |
| HTTPS | &quot;Https&quot; |



