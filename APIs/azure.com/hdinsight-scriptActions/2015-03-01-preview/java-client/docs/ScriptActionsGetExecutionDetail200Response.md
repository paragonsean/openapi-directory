

# ScriptActionsGetExecutionDetail200Response

The execution details of a script action.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**applicationName** | **String** | The application name of the script action, if any. |  [optional] [readonly] |
|**name** | **String** | The name of the script action. |  |
|**parameters** | **String** | The parameters for the script |  [optional] |
|**roles** | **List&lt;String&gt;** | The list of roles where script will be executed. |  |
|**uri** | **String** | The URI to the script. |  |
|**debugInformation** | **String** | The script action execution debug information. |  [optional] [readonly] |
|**endTime** | **String** | The end time of script action execution. |  [optional] [readonly] |
|**executionSummary** | [**List&lt;ScriptActionsGetExecutionDetail200ResponseAllOfExecutionSummaryInner&gt;**](ScriptActionsGetExecutionDetail200ResponseAllOfExecutionSummaryInner.md) | The summary of script action execution result. |  [optional] [readonly] |
|**operation** | **String** | The reason why the script action was executed. |  [optional] [readonly] |
|**scriptExecutionId** | **Long** | The execution id of the script action. |  [optional] [readonly] |
|**startTime** | **String** | The start time of script action execution. |  [optional] [readonly] |
|**status** | **String** | The current execution status of the script action. |  [optional] [readonly] |



