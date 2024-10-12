

# GetDeviceSwitchPortsStatuses200ResponseInnerSecurePort

The Secure Port status of the port.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**active** | **Boolean** | Whether Secure Port is currently active for this port. |  [optional] |
|**authenticationStatus** | [**AuthenticationStatusEnum**](#AuthenticationStatusEnum) | The current Secure Port status. |  [optional] |
|**configOverrides** | [**GetDeviceSwitchPortsStatuses200ResponseInnerSecurePortConfigOverrides**](GetDeviceSwitchPortsStatuses200ResponseInnerSecurePortConfigOverrides.md) |  |  [optional] |
|**enabled** | **Boolean** | Whether Secure Port is turned on for this port. |  [optional] |



## Enum: AuthenticationStatusEnum

| Name | Value |
|---- | -----|
| AUTHENTICATION_FAILURE | &quot;Authentication failure&quot; |
| AUTHENTICATION_IN_PROGRESS | &quot;Authentication in progress&quot; |
| AUTHENTICATION_SUCCESSFUL | &quot;Authentication successful&quot; |
| AUTHENTICATION_TIMED_OUT | &quot;Authentication timed out&quot; |
| DISABLED | &quot;Disabled&quot; |
| ENABLED | &quot;Enabled&quot; |



