# DialogflowApi.GoogleCloudDialogflowV2beta1AnalyzeContentResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**automatedAgentReply** | [**GoogleCloudDialogflowV2beta1AutomatedAgentReply**](GoogleCloudDialogflowV2beta1AutomatedAgentReply.md) |  | [optional] 
**dtmfParameters** | [**GoogleCloudDialogflowV2beta1DtmfParameters**](GoogleCloudDialogflowV2beta1DtmfParameters.md) |  | [optional] 
**endUserSuggestionResults** | [**[GoogleCloudDialogflowV2beta1SuggestionResult]**](GoogleCloudDialogflowV2beta1SuggestionResult.md) | The suggestions for end user. The order is the same as HumanAgentAssistantConfig.SuggestionConfig.feature_configs of HumanAgentAssistantConfig.end_user_suggestion_config. Same as human_agent_suggestion_results, any failure of Agent Assist features will not lead to the overall failure of an AnalyzeContent API call. Instead, the features will fail silently with the error field set in the corresponding SuggestionResult. | [optional] 
**humanAgentSuggestionResults** | [**[GoogleCloudDialogflowV2beta1SuggestionResult]**](GoogleCloudDialogflowV2beta1SuggestionResult.md) | The suggestions for most recent human agent. The order is the same as HumanAgentAssistantConfig.SuggestionConfig.feature_configs of HumanAgentAssistantConfig.human_agent_suggestion_config. Note that any failure of Agent Assist features will not lead to the overall failure of an AnalyzeContent API call. Instead, the features will fail silently with the error field set in the corresponding SuggestionResult. | [optional] 
**message** | [**GoogleCloudDialogflowV2beta1Message**](GoogleCloudDialogflowV2beta1Message.md) |  | [optional] 
**replyAudio** | [**GoogleCloudDialogflowV2beta1OutputAudio**](GoogleCloudDialogflowV2beta1OutputAudio.md) |  | [optional] 
**replyText** | **String** | Output only. The output text content. This field is set if the automated agent responded with text to show to the user. | [optional] 


