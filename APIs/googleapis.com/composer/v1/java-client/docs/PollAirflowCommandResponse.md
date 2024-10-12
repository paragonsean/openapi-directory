

# PollAirflowCommandResponse

Response to PollAirflowCommandRequest.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**exitInfo** | [**ExitInfo**](ExitInfo.md) |  |  [optional] |
|**output** | [**List&lt;Line&gt;**](Line.md) | Output from the command execution. It may not contain the full output and the caller may need to poll for more lines. |  [optional] |
|**outputEnd** | **Boolean** | Whether the command execution has finished and there is no more output. |  [optional] |



