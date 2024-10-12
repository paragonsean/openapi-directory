# DialogflowApi.GoogleCloudDialogflowV2beta1GenerateStatelessSummaryRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conversationProfile** | [**GoogleCloudDialogflowV2beta1ConversationProfile**](GoogleCloudDialogflowV2beta1ConversationProfile.md) |  | [optional] 
**latestMessage** | **String** | The name of the latest conversation message used as context for generating a Summary. If empty, the latest message of the conversation will be used. The format is specific to the user and the names of the messages provided. | [optional] 
**maxContextSize** | **Number** | Max number of messages prior to and including [latest_message] to use as context when compiling the suggestion. By default 500 and at most 1000. | [optional] 
**statelessConversation** | [**GoogleCloudDialogflowV2beta1GenerateStatelessSummaryRequestMinimalConversation**](GoogleCloudDialogflowV2beta1GenerateStatelessSummaryRequestMinimalConversation.md) |  | [optional] 


