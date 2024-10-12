

# ApplicationGatewayBackendHttpSettingsPropertiesFormat

Properties of Backend address pool settings of an application gateway.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**authenticationCertificates** | [**List&lt;ApplicationGatewayHttpListenerPropertiesFormatFrontendPort&gt;**](ApplicationGatewayHttpListenerPropertiesFormatFrontendPort.md) | Array of references to application gateway authentication certificates. |  [optional] |
|**connectionDraining** | [**ApplicationGatewayConnectionDraining**](ApplicationGatewayConnectionDraining.md) |  |  [optional] |
|**cookieBasedAffinity** | [**CookieBasedAffinityEnum**](#CookieBasedAffinityEnum) | Cookie based affinity. |  [optional] |
|**port** | **Integer** | Port |  [optional] |
|**probe** | [**ApplicationGatewayHttpListenerPropertiesFormatFrontendPort**](ApplicationGatewayHttpListenerPropertiesFormatFrontendPort.md) |  |  [optional] |
|**protocol** | [**ProtocolEnum**](#ProtocolEnum) | Protocol. |  [optional] |
|**provisioningState** | **String** | Provisioning state of the backend http settings resource. Possible values are: &#39;Updating&#39;, &#39;Deleting&#39;, and &#39;Failed&#39;. |  [optional] |
|**requestTimeout** | **Integer** | Request timeout in seconds. Application Gateway will fail the request if response is not received within RequestTimeout. Acceptable values are from 1 second to 86400 seconds. |  [optional] |



## Enum: CookieBasedAffinityEnum

| Name | Value |
|---- | -----|
| ENABLED | &quot;Enabled&quot; |
| DISABLED | &quot;Disabled&quot; |



## Enum: ProtocolEnum

| Name | Value |
|---- | -----|
| HTTP | &quot;Http&quot; |
| HTTPS | &quot;Https&quot; |



