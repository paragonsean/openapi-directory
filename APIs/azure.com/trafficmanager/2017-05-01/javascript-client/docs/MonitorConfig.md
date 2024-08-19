# TrafficManagerManagementClient.MonitorConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**intervalInSeconds** | **Number** | The monitor interval for endpoints in this profile. This is the interval at which Traffic Manager will check the health of each endpoint in this profile. | [optional] 
**path** | **String** | The path relative to the endpoint domain name used to probe for endpoint health. | [optional] 
**port** | **Number** | The TCP port used to probe for endpoint health. | [optional] 
**profileMonitorStatus** | **String** | The profile-level monitoring status of the Traffic Manager profile. | [optional] 
**protocol** | **String** | The protocol (HTTP, HTTPS or TCP) used to probe for endpoint health. | [optional] 
**timeoutInSeconds** | **Number** | The monitor timeout for endpoints in this profile. This is the time that Traffic Manager allows endpoints in this profile to response to the health check. | [optional] 
**toleratedNumberOfFailures** | **Number** | The number of consecutive failed health check that Traffic Manager tolerates before declaring an endpoint in this profile Degraded after the next failed health check. | [optional] 



## Enum: ProfileMonitorStatusEnum


* `CheckingEndpoints` (value: `"CheckingEndpoints"`)

* `Online` (value: `"Online"`)

* `Degraded` (value: `"Degraded"`)

* `Disabled` (value: `"Disabled"`)

* `Inactive` (value: `"Inactive"`)





## Enum: ProtocolEnum


* `HTTP` (value: `"HTTP"`)

* `HTTPS` (value: `"HTTPS"`)

* `TCP` (value: `"TCP"`)




