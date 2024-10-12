# FrontDoorManagementClient.HealthProbeSettingsProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resourceState** | [**ResourceState**](ResourceState.md) |  | [optional] 
**intervalInSeconds** | **Number** | The number of seconds between health probes. | [optional] 
**path** | **String** | The path to use for the health probe. Default is / | [optional] 
**protocol** | **String** | Protocol scheme to use for this probe | [optional] 



## Enum: ProtocolEnum


* `Http` (value: `"Http"`)

* `Https` (value: `"Https"`)




