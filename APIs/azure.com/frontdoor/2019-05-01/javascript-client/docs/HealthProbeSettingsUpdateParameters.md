# FrontDoorManagementClient.HealthProbeSettingsUpdateParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabledState** | **String** | Whether to enable health probes to be made against backends defined under backendPools. Health probes can only be disabled if there is a single enabled backend in single enabled backend pool. | [optional] 
**healthProbeMethod** | **String** | Configures which HTTP method to use to probe the backends defined under backendPools. | [optional] [default to &#39;HEAD&#39;]
**intervalInSeconds** | **Number** | The number of seconds between health probes. | [optional] 
**path** | **String** | The path to use for the health probe. Default is / | [optional] 
**protocol** | **String** | Protocol scheme to use for this probe | [optional] 



## Enum: EnabledStateEnum


* `Enabled` (value: `"Enabled"`)

* `Disabled` (value: `"Disabled"`)





## Enum: HealthProbeMethodEnum


* `GET` (value: `"GET"`)

* `HEAD` (value: `"HEAD"`)





## Enum: ProtocolEnum


* `Http` (value: `"Http"`)

* `Https` (value: `"Https"`)




