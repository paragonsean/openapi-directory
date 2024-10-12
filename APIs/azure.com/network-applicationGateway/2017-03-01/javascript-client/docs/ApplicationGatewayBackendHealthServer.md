# NetworkManagementClient.ApplicationGatewayBackendHealthServer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **String** | IP address or FQDN of backend server. | [optional] 
**health** | **String** | Health of backend server. | [optional] 
**ipConfiguration** | [**ApplicationGatewayHttpListenerPropertiesFormatFrontendPort**](ApplicationGatewayHttpListenerPropertiesFormatFrontendPort.md) |  | [optional] 



## Enum: HealthEnum


* `Unknown` (value: `"Unknown"`)

* `Up` (value: `"Up"`)

* `Down` (value: `"Down"`)

* `Partial` (value: `"Partial"`)

* `Draining` (value: `"Draining"`)




