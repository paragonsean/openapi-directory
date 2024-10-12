

# ApplicationGatewayBackendHealthServer

Application gateway backendhealth http settings.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**address** | **String** | IP address or FQDN of backend server. |  [optional] |
|**health** | [**HealthEnum**](#HealthEnum) | Health of backend server. Possible values are: &#39;Unknown&#39;, &#39;Up&#39;, &#39;Down&#39;, and &#39;Partial&#39;. |  [optional] |
|**ipConfiguration** | [**ApplicationGatewayHttpListenerPropertiesFormatFrontendPort**](ApplicationGatewayHttpListenerPropertiesFormatFrontendPort.md) |  |  [optional] |



## Enum: HealthEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;Unknown&quot; |
| UP | &quot;Up&quot; |
| DOWN | &quot;Down&quot; |
| PARTIAL | &quot;Partial&quot; |



