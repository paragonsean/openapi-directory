# DialogflowApi.GoogleCloudDialogflowV2beta1GenerateStatelessSummaryResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contextSize** | **Number** | Number of messages prior to and including last_conversation_message used to compile the suggestion. It may be smaller than the GenerateStatelessSummaryRequest.context_size field in the request if there weren&#39;t that many messages in the conversation. | [optional] 
**latestMessage** | **String** | The name of the latest conversation message used as context for compiling suggestion. The format is specific to the user and the names of the messages provided. | [optional] 
**summary** | [**GoogleCloudDialogflowV2beta1GenerateStatelessSummaryResponseSummary**](GoogleCloudDialogflowV2beta1GenerateStatelessSummaryResponseSummary.md) |  | [optional] 


