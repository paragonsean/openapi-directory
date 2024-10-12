# NetworkManagementClient.ApplicationGatewayBackendHttpSettingsPropertiesFormat

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authenticationCertificates** | [**[SubResource]**](SubResource.md) | Array of references to Application Gateway Authentication Certificates | [optional] 
**cookieBasedAffinity** | **String** | Cookie affinity | [optional] 
**port** | **Number** | Port | [optional] 
**probe** | [**SubResource**](SubResource.md) |  | [optional] 
**protocol** | **String** | Protocol | [optional] 
**provisioningState** | **String** | Provisioning state of the backend http settings resource Updating/Deleting/Failed | [optional] 
**requestTimeout** | **Number** | Request timeout | [optional] 



## Enum: CookieBasedAffinityEnum


* `Enabled` (value: `"Enabled"`)

* `Disabled` (value: `"Disabled"`)





## Enum: ProtocolEnum


* `Http` (value: `"Http"`)

* `Https` (value: `"Https"`)




