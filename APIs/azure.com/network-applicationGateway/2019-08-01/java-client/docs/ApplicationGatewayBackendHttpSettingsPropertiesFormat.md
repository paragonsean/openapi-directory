

# ApplicationGatewayBackendHttpSettingsPropertiesFormat

Properties of Backend address pool settings of an application gateway.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**affinityCookieName** | **String** | Cookie name to use for the affinity cookie. |  [optional] |
|**authenticationCertificates** | [**List&lt;ApplicationGatewayPathRulePropertiesFormatRewriteRuleSet&gt;**](ApplicationGatewayPathRulePropertiesFormatRewriteRuleSet.md) | Array of references to application gateway authentication certificates. |  [optional] |
|**connectionDraining** | [**ApplicationGatewayConnectionDraining**](ApplicationGatewayConnectionDraining.md) |  |  [optional] |
|**cookieBasedAffinity** | [**CookieBasedAffinityEnum**](#CookieBasedAffinityEnum) | Cookie based affinity. |  [optional] |
|**hostName** | **String** | Host header to be sent to the backend servers. |  [optional] |
|**path** | **String** | Path which should be used as a prefix for all HTTP requests. Null means no path will be prefixed. Default value is null. |  [optional] |
|**pickHostNameFromBackendAddress** | **Boolean** | Whether to pick host header should be picked from the host name of the backend server. Default value is false. |  [optional] |
|**port** | **Integer** | The destination port on the backend. |  [optional] |
|**probe** | [**ApplicationGatewayPathRulePropertiesFormatRewriteRuleSet**](ApplicationGatewayPathRulePropertiesFormatRewriteRuleSet.md) |  |  [optional] |
|**probeEnabled** | **Boolean** | Whether the probe is enabled. Default value is false. |  [optional] |
|**protocol** | **ApplicationGatewayProtocol** |  |  [optional] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | The current provisioning state. |  [optional] [readonly] |
|**requestTimeout** | **Integer** | Request timeout in seconds. Application Gateway will fail the request if response is not received within RequestTimeout. Acceptable values are from 1 second to 86400 seconds. |  [optional] |
|**trustedRootCertificates** | [**List&lt;ApplicationGatewayPathRulePropertiesFormatRewriteRuleSet&gt;**](ApplicationGatewayPathRulePropertiesFormatRewriteRuleSet.md) | Array of references to application gateway trusted root certificates. |  [optional] |



## Enum: CookieBasedAffinityEnum

| Name | Value |
|---- | -----|
| ENABLED | &quot;Enabled&quot; |
| DISABLED | &quot;Disabled&quot; |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| SUCCEEDED | &quot;Succeeded&quot; |
| UPDATING | &quot;Updating&quot; |
| DELETING | &quot;Deleting&quot; |
| FAILED | &quot;Failed&quot; |



