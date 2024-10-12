

# GoogleCloudAiplatformV1beta1InternalOsServiceStateInstance

Request message for [InternalOsServiceStateInstance].

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**serviceName** | [**ServiceNameEnum**](#ServiceNameEnum) | Required. internal service name. |  [optional] |
|**serviceState** | [**ServiceStateEnum**](#ServiceStateEnum) | Required. internal service state. |  [optional] |



## Enum: ServiceNameEnum

| Name | Value |
|---- | -----|
| INTERNAL_OS_SERVICE_ENUM_UNSPECIFIED | &quot;INTERNAL_OS_SERVICE_ENUM_UNSPECIFIED&quot; |
| DOCKER_SERVICE_STATE | &quot;DOCKER_SERVICE_STATE&quot; |
| CONTROL_PLANE_API_DNS_STATE | &quot;CONTROL_PLANE_API_DNS_STATE&quot; |
| PROXY_REGISTRATION_DNS_STATE | &quot;PROXY_REGISTRATION_DNS_STATE&quot; |
| JUPYTER_STATE | &quot;JUPYTER_STATE&quot; |
| JUPYTER_API_STATE | &quot;JUPYTER_API_STATE&quot; |
| EUC_METADATA_API_STATE | &quot;EUC_METADATA_API_STATE&quot; |
| EUC_AGENT_API_STATE | &quot;EUC_AGENT_API_STATE&quot; |
| IDLE_SHUTDOWN_AGENT_STATE | &quot;IDLE_SHUTDOWN_AGENT_STATE&quot; |
| PROXY_AGENT_STATE | &quot;PROXY_AGENT_STATE&quot; |



## Enum: ServiceStateEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;UNKNOWN&quot; |
| HEALTHY | &quot;HEALTHY&quot; |
| UNHEALTHY | &quot;UNHEALTHY&quot; |



