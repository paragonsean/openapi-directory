

# LogAnalytics

Container group log analytics information.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**logType** | [**LogTypeEnum**](#LogTypeEnum) | The log type to be used. |  [optional] |
|**metadata** | **Map&lt;String, String&gt;** | Metadata for log analytics. |  [optional] |
|**workspaceId** | **String** | The workspace id for log analytics |  |
|**workspaceKey** | **String** | The workspace key for log analytics |  |



## Enum: LogTypeEnum

| Name | Value |
|---- | -----|
| CONTAINER_INSIGHTS | &quot;ContainerInsights&quot; |
| CONTAINER_INSTANCE_LOGS | &quot;ContainerInstanceLogs&quot; |



