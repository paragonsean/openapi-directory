# NetworkManagementClient.ApplicationGatewayBackendHttpSettingsPropertiesFormat

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authenticationCertificates** | [**[ApplicationGatewayHttpListenerPropertiesFormatFrontendPort]**](ApplicationGatewayHttpListenerPropertiesFormatFrontendPort.md) | Array of references to application gateway authentication certificates. | [optional] 
**connectionDraining** | [**ApplicationGatewayConnectionDraining**](ApplicationGatewayConnectionDraining.md) |  | [optional] 
**cookieBasedAffinity** | **String** | Cookie based affinity. | [optional] 
**port** | **Number** | Port | [optional] 
**probe** | [**ApplicationGatewayHttpListenerPropertiesFormatFrontendPort**](ApplicationGatewayHttpListenerPropertiesFormatFrontendPort.md) |  | [optional] 
**protocol** | **String** | Protocol. | [optional] 
**provisioningState** | **String** | Provisioning state of the backend http settings resource. Possible values are: &#39;Updating&#39;, &#39;Deleting&#39;, and &#39;Failed&#39;. | [optional] 
**requestTimeout** | **Number** | Request timeout in seconds. Application Gateway will fail the request if response is not received within RequestTimeout. Acceptable values are from 1 second to 86400 seconds. | [optional] 



## Enum: CookieBasedAffinityEnum


* `Enabled` (value: `"Enabled"`)

* `Disabled` (value: `"Disabled"`)





## Enum: ProtocolEnum


* `Http` (value: `"Http"`)

* `Https` (value: `"Https"`)




