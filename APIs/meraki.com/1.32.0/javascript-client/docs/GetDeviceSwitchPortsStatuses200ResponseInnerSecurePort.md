# MerakiDashboardApi.GetDeviceSwitchPortsStatuses200ResponseInnerSecurePort

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **Boolean** | Whether Secure Port is currently active for this port. | [optional] 
**authenticationStatus** | **String** | The current Secure Port status. | [optional] 
**configOverrides** | [**GetDeviceSwitchPortsStatuses200ResponseInnerSecurePortConfigOverrides**](GetDeviceSwitchPortsStatuses200ResponseInnerSecurePortConfigOverrides.md) |  | [optional] 
**enabled** | **Boolean** | Whether Secure Port is turned on for this port. | [optional] 



## Enum: AuthenticationStatusEnum


* `Authentication failure` (value: `"Authentication failure"`)

* `Authentication in progress` (value: `"Authentication in progress"`)

* `Authentication successful` (value: `"Authentication successful"`)

* `Authentication timed out` (value: `"Authentication timed out"`)

* `Disabled` (value: `"Disabled"`)

* `Enabled` (value: `"Enabled"`)




