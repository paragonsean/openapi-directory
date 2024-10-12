

# ReportExecutionProperties

The properties of the report execution.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**executionType** | [**ExecutionTypeEnum**](#ExecutionTypeEnum) | The type of the report execution. |  [optional] |
|**fileName** | **String** | The name of the file report got written to. |  [optional] |
|**processingEndTime** | **OffsetDateTime** | The time when report execution finished. |  [optional] |
|**processingStartTime** | **OffsetDateTime** | The time when report was picked up to be executed. |  [optional] |
|**reportSettings** | [**CommonReportProperties**](CommonReportProperties.md) |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The status of the report execution. |  [optional] |
|**submittedBy** | **String** | The identifier for the entity that executed the report. For OnDemand executions, it is the email id. For Scheduled executions, it is the constant value - System. |  [optional] |
|**submittedTime** | **OffsetDateTime** | The time when report was queued to be executed. |  [optional] |



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



