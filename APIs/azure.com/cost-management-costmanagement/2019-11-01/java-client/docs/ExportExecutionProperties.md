

# ExportExecutionProperties

The properties of the export execution.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**executionType** | [**ExecutionTypeEnum**](#ExecutionTypeEnum) | The type of the export execution. |  [optional] |
|**fileName** | **String** | The name of the file export got written to. |  [optional] |
|**processingEndTime** | **OffsetDateTime** | The time when export execution finished. |  [optional] |
|**processingStartTime** | **OffsetDateTime** | The time when export was picked up to be executed. |  [optional] |
|**runSettings** | [**CommonExportProperties**](CommonExportProperties.md) |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The status of the export execution. |  [optional] |
|**submittedBy** | **String** | The identifier for the entity that executed the export. For OnDemand executions, it is the email id. For Scheduled executions, it is the constant value - System. |  [optional] |
|**submittedTime** | **OffsetDateTime** | The time when export was queued to be executed. |  [optional] |



## Enum: ExecutionTypeEnum

| Name | Value |
|---- | -----|
| ON_DEMAND | &quot;OnDemand&quot; |
| SCHEDULED | &quot;Scheduled&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| QUEUED | &quot;Queued&quot; |
| IN_PROGRESS | &quot;InProgress&quot; |
| COMPLETED | &quot;Completed&quot; |
| FAILED | &quot;Failed&quot; |
| TIMEOUT | &quot;Timeout&quot; |
| NEW_DATA_NOT_AVAILABLE | &quot;NewDataNotAvailable&quot; |
| DATA_NOT_AVAILABLE | &quot;DataNotAvailable&quot; |



