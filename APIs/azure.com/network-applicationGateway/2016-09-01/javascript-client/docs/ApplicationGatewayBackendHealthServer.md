# NetworkManagementClient.ApplicationGatewayBackendHealthServer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **String** | IP address or FQDN of backend server. | [optional] 
**health** | **String** | Health of backend server. Possible values are: &#39;Unknown&#39;, &#39;Up&#39;, &#39;Down&#39;, and &#39;Partial&#39;. | [optional] 
**ipConfiguration** | [**ApplicationGatewayHttpListenerPropertiesFormatFrontendPort**](ApplicationGatewayHttpListenerPropertiesFormatFrontendPort.md) |  | [optional] 



## Enum: HealthEnum


* `Unknown` (value: `"Unknown"`)

* `Up` (value: `"Up"`)

* `Down` (value: `"Down"`)

* `Partial` (value: `"Partial"`)




