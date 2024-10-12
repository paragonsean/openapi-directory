# DialogflowApi.GoogleCloudDialogflowCxV3beta1ConversationTurnVirtualAgentOutput

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currentPage** | [**GoogleCloudDialogflowCxV3beta1Page**](GoogleCloudDialogflowCxV3beta1Page.md) |  | [optional] 
**diagnosticInfo** | **{String: Object}** | Required. Input only. The diagnostic info output for the turn. Required to calculate the testing coverage. | [optional] 
**differences** | [**[GoogleCloudDialogflowCxV3beta1TestRunDifference]**](GoogleCloudDialogflowCxV3beta1TestRunDifference.md) | Output only. If this is part of a result conversation turn, the list of differences between the original run and the replay for this output, if any. | [optional] [readonly] 
**sessionParameters** | **{String: Object}** | The session parameters available to the bot at this point. | [optional] 
**status** | [**GoogleRpcStatus**](GoogleRpcStatus.md) |  | [optional] 
**textResponses** | [**[GoogleCloudDialogflowCxV3beta1ResponseMessageText]**](GoogleCloudDialogflowCxV3beta1ResponseMessageText.md) | The text responses from the agent for the turn. | [optional] 
**triggeredIntent** | [**GoogleCloudDialogflowCxV3beta1Intent**](GoogleCloudDialogflowCxV3beta1Intent.md) |  | [optional] 


