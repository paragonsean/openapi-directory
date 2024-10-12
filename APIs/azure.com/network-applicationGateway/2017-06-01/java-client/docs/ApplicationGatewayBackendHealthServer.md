

# ApplicationGatewayBackendHealthServer

Application gateway backendhealth http settings.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**address** | **String** | IP address or FQDN of backend server. |  [optional] |
|**health** | [**HealthEnum**](#HealthEnum) | Health of backend server. |  [optional] |
|**ipConfiguration** | [**ApplicationGatewayBackendHealthServerIpConfiguration**](ApplicationGatewayBackendHealthServerIpConfiguration.md) |  |  [optional] |



## Enum: HealthEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;Unknown&quot; |
| UP | &quot;Up&quot; |
| DOWN | &quot;Down&quot; |
| PARTIAL | &quot;Partial&quot; |
| DRAINING | &quot;Draining&quot; |



