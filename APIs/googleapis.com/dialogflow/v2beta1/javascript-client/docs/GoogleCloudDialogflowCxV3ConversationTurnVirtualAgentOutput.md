# DialogflowApi.GoogleCloudDialogflowCxV3ConversationTurnVirtualAgentOutput

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currentPage** | [**GoogleCloudDialogflowCxV3Page**](GoogleCloudDialogflowCxV3Page.md) |  | [optional] 
**diagnosticInfo** | **{String: Object}** | Required. Input only. The diagnostic info output for the turn. Required to calculate the testing coverage. | [optional] 
**differences** | [**[GoogleCloudDialogflowCxV3TestRunDifference]**](GoogleCloudDialogflowCxV3TestRunDifference.md) | Output only. If this is part of a result conversation turn, the list of differences between the original run and the replay for this output, if any. | [optional] [readonly] 
**sessionParameters** | **{String: Object}** | The session parameters available to the bot at this point. | [optional] 
**status** | [**GoogleRpcStatus**](GoogleRpcStatus.md) |  | [optional] 
**textResponses** | [**[GoogleCloudDialogflowCxV3ResponseMessageText]**](GoogleCloudDialogflowCxV3ResponseMessageText.md) | The text responses from the agent for the turn. | [optional] 
**triggeredIntent** | [**GoogleCloudDialogflowCxV3Intent**](GoogleCloudDialogflowCxV3Intent.md) |  | [optional] 


