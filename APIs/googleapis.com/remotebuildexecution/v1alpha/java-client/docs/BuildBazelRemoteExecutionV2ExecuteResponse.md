

# BuildBazelRemoteExecutionV2ExecuteResponse

The response message for Execution.Execute, which will be contained in the response field of the Operation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cachedResult** | **Boolean** | True if the result was served from cache, false if it was executed. |  [optional] |
|**message** | **String** | Freeform informational message with details on the execution of the action that may be displayed to the user upon failure or when requested explicitly. |  [optional] |
|**result** | [**BuildBazelRemoteExecutionV2ActionResult**](BuildBazelRemoteExecutionV2ActionResult.md) |  |  [optional] |
|**serverLogs** | [**Map&lt;String, BuildBazelRemoteExecutionV2LogFile&gt;**](BuildBazelRemoteExecutionV2LogFile.md) | An optional list of additional log outputs the server wishes to provide. A server can use this to return execution-specific logs however it wishes. This is intended primarily to make it easier for users to debug issues that may be outside of the actual job execution, such as by identifying the worker executing the action or by providing logs from the worker&#39;s setup phase. The keys SHOULD be human readable so that a client can display them to a user. |  [optional] |
|**status** | [**GoogleRpcStatus**](GoogleRpcStatus.md) |  |  [optional] |



