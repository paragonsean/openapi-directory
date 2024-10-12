# NetworkManagementClient.ApplicationGatewayBackendHttpSettingsPropertiesFormat

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cookieBasedAffinity** | **String** | Gets or sets the cookie affinity | [optional] 
**port** | **Number** | Gets or sets the port | [optional] 
**probe** | [**SubResource**](SubResource.md) |  | [optional] 
**protocol** | **String** | Gets or sets the protocol | [optional] 
**provisioningState** | **String** | Gets or sets Provisioning state of the backend http settings resource Updating/Deleting/Failed | [optional] 
**requestTimeout** | **Number** | Gets or sets request timeout | [optional] 



## Enum: CookieBasedAffinityEnum


* `Enabled` (value: `"Enabled"`)

* `Disabled` (value: `"Disabled"`)





## Enum: ProtocolEnum


* `Http` (value: `"Http"`)

* `Https` (value: `"Https"`)




