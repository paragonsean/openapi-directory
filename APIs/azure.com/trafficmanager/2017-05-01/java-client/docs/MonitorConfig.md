

# MonitorConfig

Class containing endpoint monitoring settings in a Traffic Manager profile.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**intervalInSeconds** | **Long** | The monitor interval for endpoints in this profile. This is the interval at which Traffic Manager will check the health of each endpoint in this profile. |  [optional] |
|**path** | **String** | The path relative to the endpoint domain name used to probe for endpoint health. |  [optional] |
|**port** | **Long** | The TCP port used to probe for endpoint health. |  [optional] |
|**profileMonitorStatus** | [**ProfileMonitorStatusEnum**](#ProfileMonitorStatusEnum) | The profile-level monitoring status of the Traffic Manager profile. |  [optional] |
|**protocol** | [**ProtocolEnum**](#ProtocolEnum) | The protocol (HTTP, HTTPS or TCP) used to probe for endpoint health. |  [optional] |
|**timeoutInSeconds** | **Long** | The monitor timeout for endpoints in this profile. This is the time that Traffic Manager allows endpoints in this profile to response to the health check. |  [optional] |
|**toleratedNumberOfFailures** | **Long** | The number of consecutive failed health check that Traffic Manager tolerates before declaring an endpoint in this profile Degraded after the next failed health check. |  [optional] |



## Enum: ProfileMonitorStatusEnum

| Name | Value |
|---- | -----|
| CHECKING_ENDPOINTS | &quot;CheckingEndpoints&quot; |
| ONLINE | &quot;Online&quot; |
| DEGRADED | &quot;Degraded&quot; |
| DISABLED | &quot;Disabled&quot; |
| INACTIVE | &quot;Inactive&quot; |



## Enum: ProtocolEnum

| Name | Value |
|---- | -----|
| HTTP | &quot;HTTP&quot; |
| HTTPS | &quot;HTTPS&quot; |
| TCP | &quot;TCP&quot; |



