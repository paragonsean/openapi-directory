# NetworkManagementClient.ApplicationGatewayBackendHttpSettingsPropertiesFormat

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affinityCookieName** | **String** | Cookie name to use for the affinity cookie. | [optional] 
**authenticationCertificates** | [**[ApplicationGatewayPathRulePropertiesFormatRedirectConfiguration]**](ApplicationGatewayPathRulePropertiesFormatRedirectConfiguration.md) | Array of references to application gateway authentication certificates. | [optional] 
**connectionDraining** | [**ApplicationGatewayConnectionDraining**](ApplicationGatewayConnectionDraining.md) |  | [optional] 
**cookieBasedAffinity** | **String** | Cookie based affinity. | [optional] 
**hostName** | **String** | Host header to be sent to the backend servers. | [optional] 
**path** | **String** | Path which should be used as a prefix for all HTTP requests. Null means no path will be prefixed. Default value is null. | [optional] 
**pickHostNameFromBackendAddress** | **Boolean** | Whether to pick host header should be picked from the host name of the backend server. Default value is false. | [optional] 
**port** | **Number** | The destination port on the backend. | [optional] 
**probe** | [**ApplicationGatewayPathRulePropertiesFormatRedirectConfiguration**](ApplicationGatewayPathRulePropertiesFormatRedirectConfiguration.md) |  | [optional] 
**probeEnabled** | **Boolean** | Whether the probe is enabled. Default value is false. | [optional] 
**protocol** | **String** | The protocol used to communicate with the backend. Possible values are &#39;Http&#39; and &#39;Https&#39;. | [optional] 
**provisioningState** | **String** | Provisioning state of the backend http settings resource. Possible values are: &#39;Updating&#39;, &#39;Deleting&#39;, and &#39;Failed&#39;. | [optional] 
**requestTimeout** | **Number** | Request timeout in seconds. Application Gateway will fail the request if response is not received within RequestTimeout. Acceptable values are from 1 second to 86400 seconds. | [optional] 
**trustedRootCertificates** | [**[ApplicationGatewayPathRulePropertiesFormatRedirectConfiguration]**](ApplicationGatewayPathRulePropertiesFormatRedirectConfiguration.md) | Array of references to application gateway trusted root certificates. | [optional] 



## Enum: CookieBasedAffinityEnum


* `Enabled` (value: `"Enabled"`)

* `Disabled` (value: `"Disabled"`)





## Enum: ProtocolEnum


* `Http` (value: `"Http"`)

* `Https` (value: `"Https"`)




