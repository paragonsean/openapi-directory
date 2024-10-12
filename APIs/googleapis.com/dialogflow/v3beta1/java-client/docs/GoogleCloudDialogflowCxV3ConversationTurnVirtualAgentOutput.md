

# GoogleCloudDialogflowCxV3ConversationTurnVirtualAgentOutput

The output from the virtual agent.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**currentPage** | [**GoogleCloudDialogflowCxV3Page**](GoogleCloudDialogflowCxV3Page.md) |  |  [optional] |
|**diagnosticInfo** | **Map&lt;String, Object&gt;** | Required. Input only. The diagnostic info output for the turn. Required to calculate the testing coverage. |  [optional] |
|**differences** | [**List&lt;GoogleCloudDialogflowCxV3TestRunDifference&gt;**](GoogleCloudDialogflowCxV3TestRunDifference.md) | Output only. If this is part of a result conversation turn, the list of differences between the original run and the replay for this output, if any. |  [optional] [readonly] |
|**sessionParameters** | **Map&lt;String, Object&gt;** | The session parameters available to the bot at this point. |  [optional] |
|**status** | [**GoogleRpcStatus**](GoogleRpcStatus.md) |  |  [optional] |
|**textResponses** | [**List&lt;GoogleCloudDialogflowCxV3ResponseMessageText&gt;**](GoogleCloudDialogflowCxV3ResponseMessageText.md) | The text responses from the agent for the turn. |  [optional] |
|**triggeredIntent** | [**GoogleCloudDialogflowCxV3Intent**](GoogleCloudDialogflowCxV3Intent.md) |  |  [optional] |



