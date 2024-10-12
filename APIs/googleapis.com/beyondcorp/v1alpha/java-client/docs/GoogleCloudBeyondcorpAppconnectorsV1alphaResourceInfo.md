

# GoogleCloudBeyondcorpAppconnectorsV1alphaResourceInfo

ResourceInfo represents the information/status of an app connector resource. Such as: - remote_agent - container - runtime - appgateway - appconnector - appconnection - tunnel - logagent

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Required. Unique Id for the resource. |  [optional] |
|**resource** | **Map&lt;String, Object&gt;** | Specific details for the resource. This is for internal use only. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Overall health status. Overall status is derived based on the status of each sub level resources. |  [optional] |
|**sub** | [**List&lt;GoogleCloudBeyondcorpAppconnectorsV1alphaResourceInfo&gt;**](GoogleCloudBeyondcorpAppconnectorsV1alphaResourceInfo.md) | List of Info for the sub level resources. |  [optional] |
|**time** | **String** | The timestamp to collect the info. It is suggested to be set by the topmost level resource only. |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| HEALTH_STATUS_UNSPECIFIED | &quot;HEALTH_STATUS_UNSPECIFIED&quot; |
| HEALTHY | &quot;HEALTHY&quot; |
| UNHEALTHY | &quot;UNHEALTHY&quot; |
| UNRESPONSIVE | &quot;UNRESPONSIVE&quot; |
| DEGRADED | &quot;DEGRADED&quot; |



