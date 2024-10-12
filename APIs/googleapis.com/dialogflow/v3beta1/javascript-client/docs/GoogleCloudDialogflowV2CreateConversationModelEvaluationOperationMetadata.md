# DialogflowApi.GoogleCloudDialogflowV2CreateConversationModelEvaluationOperationMetadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conversationModel** | **String** | The resource name of the conversation model. Format: &#x60;projects//locations//conversationModels/&#x60; | [optional] 
**conversationModelEvaluation** | **String** | The resource name of the conversation model. Format: &#x60;projects//locations//conversationModels//evaluations/&#x60; | [optional] 
**createTime** | **String** | Timestamp when the request to create conversation model was submitted. The time is measured on server side. | [optional] 
**state** | **String** | State of CreateConversationModel operation. | [optional] 



## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `INITIALIZING` (value: `"INITIALIZING"`)

* `RUNNING` (value: `"RUNNING"`)

* `CANCELLED` (value: `"CANCELLED"`)

* `SUCCEEDED` (value: `"SUCCEEDED"`)

* `FAILED` (value: `"FAILED"`)




