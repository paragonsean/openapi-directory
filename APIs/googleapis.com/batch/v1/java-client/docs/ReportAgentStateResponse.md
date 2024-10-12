

# ReportAgentStateResponse

Response to ReportAgentStateRequest.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**defaultReportInterval** | **String** | Default report interval override |  [optional] |
|**minReportInterval** | **String** | Minimum report interval override |  [optional] |
|**tasks** | [**List&lt;AgentTask&gt;**](AgentTask.md) | Tasks assigned to the agent |  [optional] |
|**useBatchMonitoredResource** | **Boolean** | If true, the cloud logging for batch agent will use batch.googleapis.com/Job as monitored resource for Batch job related logging. |  [optional] |



