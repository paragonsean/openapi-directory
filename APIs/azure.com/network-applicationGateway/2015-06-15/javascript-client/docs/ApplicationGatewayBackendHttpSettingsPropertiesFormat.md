# NetworkManagementClient.ApplicationGatewayBackendHttpSettingsPropertiesFormat

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cookieBasedAffinity** | **String** | Cookie based affinity. Possible values are: &#39;Enabled&#39; and &#39;Disabled&#39;. | [optional] 
**port** | **Number** | Port | [optional] 
**probe** | [**Model0**](Model0.md) |  | [optional] 
**protocol** | **String** | Protocol. Possible values are: &#39;Http&#39; and &#39;Https&#39;. | [optional] 
**provisioningState** | **String** | Gets or sets Provisioning state of the backend http settings resource Updating/Deleting/Failed | [optional] 
**requestTimeout** | **Number** | Request timeout in seconds. Application Gateway will fail the request if response is not received within RequestTimeout. Acceptable values are from 1 second to 86400 seconds. | [optional] 



## Enum: CookieBasedAffinityEnum


* `Enabled` (value: `"Enabled"`)

* `Disabled` (value: `"Disabled"`)





## Enum: ProtocolEnum


* `Http` (value: `"Http"`)

* `Https` (value: `"Https"`)




