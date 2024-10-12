

# ApplicationGatewayBackendHttpSettingsPropertiesFormat

Properties of Backend address pool settings of application gateway

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cookieBasedAffinity** | [**CookieBasedAffinityEnum**](#CookieBasedAffinityEnum) | Gets or sets the cookie affinity |  [optional] |
|**port** | **Integer** | Gets or sets the port |  [optional] |
|**protocol** | [**ProtocolEnum**](#ProtocolEnum) | Gets or sets the protocol |  [optional] |
|**provisioningState** | **String** | Gets or sets Provisioning state of the backend http settings resource Updating/Deleting/Failed |  [optional] |



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



