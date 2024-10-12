

# ApplicationGatewayBackendHttpSettingsPropertiesFormat

Properties of Backend address pool settings of application gateway

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**authenticationCertificates** | [**List&lt;SubResource&gt;**](SubResource.md) | Array of references to Application Gateway Authentication Certificates |  [optional] |
|**cookieBasedAffinity** | [**CookieBasedAffinityEnum**](#CookieBasedAffinityEnum) | Cookie affinity |  [optional] |
|**port** | **Integer** | Port |  [optional] |
|**probe** | [**SubResource**](SubResource.md) |  |  [optional] |
|**protocol** | [**ProtocolEnum**](#ProtocolEnum) | Protocol |  [optional] |
|**provisioningState** | **String** | Provisioning state of the backend http settings resource Updating/Deleting/Failed |  [optional] |
|**requestTimeout** | **Integer** | Request timeout |  [optional] |



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



