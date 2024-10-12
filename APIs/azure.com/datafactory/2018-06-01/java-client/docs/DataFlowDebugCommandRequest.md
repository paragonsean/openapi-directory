

# DataFlowDebugCommandRequest

Request body structure for data flow debug command.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**command** | [**CommandEnum**](#CommandEnum) | The command type. |  [optional] |
|**commandPayload** | [**DataFlowDebugCommandPayload**](DataFlowDebugCommandPayload.md) |  |  [optional] |
|**sessionId** | **String** | The ID of data flow debug session. |  [optional] |



## Enum: CommandEnum

| Name | Value |
|---- | -----|
| EXECUTE_PREVIEW_QUERY | &quot;executePreviewQuery&quot; |
| EXECUTE_STATISTICS_QUERY | &quot;executeStatisticsQuery&quot; |
| EXECUTE_EXPRESSION_QUERY | &quot;executeExpressionQuery&quot; |



