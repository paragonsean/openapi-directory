

# GoogleApiServiceusageV1Service

A service that is available for use by the consumer.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**config** | [**GoogleApiServiceusageV1ServiceConfig**](GoogleApiServiceusageV1ServiceConfig.md) |  |  [optional] |
|**name** | **String** | The resource name of the consumer and service. A valid name would be: - projects/123/services/serviceusage.googleapis.com |  [optional] |
|**parent** | **String** | The resource name of the consumer. A valid name would be: - projects/123 |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Whether or not the service has been enabled for use by the consumer. |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| DISABLED | &quot;DISABLED&quot; |
| ENABLED | &quot;ENABLED&quot; |



