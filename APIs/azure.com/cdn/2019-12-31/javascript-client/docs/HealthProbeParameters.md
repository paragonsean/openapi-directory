# CdnManagementClient.HealthProbeParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**probeIntervalInSeconds** | **Number** | The number of seconds between health probes.Default is 240sec. | [optional] 
**probePath** | **String** | The path relative to the origin that is used to determine the health of the origin. | [optional] 
**probeProtocol** | **String** | Protocol to use for health probe. | [optional] 
**probeRequestType** | **String** | The type of health probe request that is made. | [optional] 



## Enum: ProbeProtocolEnum


* `NotSet` (value: `"NotSet"`)

* `Http` (value: `"Http"`)

* `Https` (value: `"Https"`)





## Enum: ProbeRequestTypeEnum


* `NotSet` (value: `"NotSet"`)

* `GET` (value: `"GET"`)

* `HEAD` (value: `"HEAD"`)




