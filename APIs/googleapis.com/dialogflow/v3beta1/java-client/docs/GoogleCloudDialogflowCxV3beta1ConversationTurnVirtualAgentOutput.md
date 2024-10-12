

# GoogleCloudDialogflowCxV3beta1ConversationTurnVirtualAgentOutput

The output from the virtual agent.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**currentPage** | [**GoogleCloudDialogflowCxV3beta1Page**](GoogleCloudDialogflowCxV3beta1Page.md) |  |  [optional] |
|**diagnosticInfo** | **Map&lt;String, Object&gt;** | Required. Input only. The diagnostic info output for the turn. Required to calculate the testing coverage. |  [optional] |
|**differences** | [**List&lt;GoogleCloudDialogflowCxV3beta1TestRunDifference&gt;**](GoogleCloudDialogflowCxV3beta1TestRunDifference.md) | Output only. If this is part of a result conversation turn, the list of differences between the original run and the replay for this output, if any. |  [optional] [readonly] |
|**sessionParameters** | **Map&lt;String, Object&gt;** | The session parameters available to the bot at this point. |  [optional] |
|**status** | [**GoogleRpcStatus**](GoogleRpcStatus.md) |  |  [optional] |
|**textResponses** | [**List&lt;GoogleCloudDialogflowCxV3beta1ResponseMessageText&gt;**](GoogleCloudDialogflowCxV3beta1ResponseMessageText.md) | The text responses from the agent for the turn. |  [optional] |
|**triggeredIntent** | [**GoogleCloudDialogflowCxV3beta1Intent**](GoogleCloudDialogflowCxV3beta1Intent.md) |  |  [optional] |



