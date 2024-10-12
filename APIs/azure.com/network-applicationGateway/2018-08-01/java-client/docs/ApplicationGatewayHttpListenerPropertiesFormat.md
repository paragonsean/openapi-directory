

# ApplicationGatewayHttpListenerPropertiesFormat

Properties of HTTP listener of an application gateway.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**customErrorConfigurations** | [**List&lt;ApplicationGatewayCustomError&gt;**](ApplicationGatewayCustomError.md) | Custom error configurations of the HTTP listener. |  [optional] |
|**frontendIPConfiguration** | [**ApplicationGatewayPathRulePropertiesFormatRedirectConfiguration**](ApplicationGatewayPathRulePropertiesFormatRedirectConfiguration.md) |  |  [optional] |
|**frontendPort** | [**ApplicationGatewayPathRulePropertiesFormatRedirectConfiguration**](ApplicationGatewayPathRulePropertiesFormatRedirectConfiguration.md) |  |  [optional] |
|**hostName** | **String** | Host name of HTTP listener. |  [optional] |
|**protocol** | [**ProtocolEnum**](#ProtocolEnum) | Protocol of the HTTP listener. Possible values are &#39;Http&#39; and &#39;Https&#39;. |  [optional] |
|**provisioningState** | **String** | Provisioning state of the HTTP listener resource. Possible values are: &#39;Updating&#39;, &#39;Deleting&#39;, and &#39;Failed&#39;. |  [optional] |
|**requireServerNameIndication** | **Boolean** | Applicable only if protocol is https. Enables SNI for multi-hosting. |  [optional] |
|**sslCertificate** | [**ApplicationGatewayPathRulePropertiesFormatRedirectConfiguration**](ApplicationGatewayPathRulePropertiesFormatRedirectConfiguration.md) |  |  [optional] |



## Enum: ProtocolEnum

| Name | Value |
|---- | -----|
| HTTP | &quot;Http&quot; |
| HTTPS | &quot;Https&quot; |



