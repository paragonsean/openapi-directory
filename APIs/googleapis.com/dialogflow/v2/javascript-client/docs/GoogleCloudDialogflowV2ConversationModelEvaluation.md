# DialogflowApi.GoogleCloudDialogflowV2ConversationModelEvaluation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | Output only. Creation time of this model. | [optional] [readonly] 
**displayName** | **String** | Optional. The display name of the model evaluation. At most 64 bytes long. | [optional] 
**evaluationConfig** | [**GoogleCloudDialogflowV2EvaluationConfig**](GoogleCloudDialogflowV2EvaluationConfig.md) |  | [optional] 
**name** | **String** | The resource name of the evaluation. Format: &#x60;projects//conversationModels//evaluations/&#x60; | [optional] 
**rawHumanEvalTemplateCsv** | **String** | Output only. Human eval template in csv format. It tooks real-world conversations provided through input dataset, generates example suggestions for customer to verify quality of the model. For Smart Reply, the generated csv file contains columns of Context, (Suggestions,Q1,Q2)*3, Actual reply. Context contains at most 10 latest messages in the conversation prior to the current suggestion. Q1: \&quot;Would you send it as the next message of agent?\&quot; Evaluated based on whether the suggest is appropriate to be sent by agent in current context. Q2: \&quot;Does the suggestion move the conversation closer to resolution?\&quot; Evaluated based on whether the suggestion provide solutions, or answers customer&#39;s question or collect information from customer to resolve the customer&#39;s issue. Actual reply column contains the actual agent reply sent in the context. | [optional] [readonly] 
**smartReplyMetrics** | [**GoogleCloudDialogflowV2SmartReplyMetrics**](GoogleCloudDialogflowV2SmartReplyMetrics.md) |  | [optional] 


