

# TriggerRun

Trigger runs.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dependencyStatus** | **Map&lt;String, Object&gt;** | Status of the upstream pipelines. |  [optional] [readonly] |
|**message** | **String** | Trigger error message. |  [optional] [readonly] |
|**properties** | **Map&lt;String, String&gt;** | List of property name and value related to trigger run. Name, value pair depends on type of trigger. |  [optional] [readonly] |
|**runDimension** | **Map&lt;String, String&gt;** | Run dimension for which trigger was fired. |  [optional] [readonly] |
|**status** | [**StatusEnum**](#StatusEnum) | Trigger run status. |  [optional] [readonly] |
|**triggerName** | **String** | Trigger name. |  [optional] [readonly] |
|**triggerRunId** | **String** | Trigger run id. |  [optional] [readonly] |
|**triggerRunTimestamp** | **OffsetDateTime** | Trigger run start time. |  [optional] [readonly] |
|**triggerType** | **String** | Trigger type. |  [optional] [readonly] |
|**triggeredPipelines** | **Map&lt;String, String&gt;** | List of pipeline name and run Id triggered by the trigger run. |  [optional] [readonly] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| SUCCEEDED | &quot;Succeeded&quot; |
| FAILED | &quot;Failed&quot; |
| INPROGRESS | &quot;Inprogress&quot; |



