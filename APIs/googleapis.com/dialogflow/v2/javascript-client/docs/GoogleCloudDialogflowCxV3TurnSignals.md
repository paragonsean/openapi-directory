# DialogflowApi.GoogleCloudDialogflowCxV3TurnSignals

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agentEscalated** | **Boolean** | Whether agent responded with LiveAgentHandoff fulfillment. | [optional] 
**dtmfUsed** | **Boolean** | Whether user was using DTMF input. | [optional] 
**failureReasons** | **[String]** | Failure reasons of the turn. | [optional] 
**noMatch** | **Boolean** | Whether NLU predicted NO_MATCH. | [optional] 
**noUserInput** | **Boolean** | Whether user provided no input. | [optional] 
**reachedEndPage** | **Boolean** | Whether turn resulted in End Session page. | [optional] 
**sentimentMagnitude** | **Number** | Sentiment magnitude of the user utterance if [sentiment](https://cloud.google.com/dialogflow/cx/docs/concept/sentiment) was enabled. | [optional] 
**sentimentScore** | **Number** | Sentiment score of the user utterance if [sentiment](https://cloud.google.com/dialogflow/cx/docs/concept/sentiment) was enabled. | [optional] 
**userEscalated** | **Boolean** | Whether user was specifically asking for a live agent. | [optional] 
**webhookStatuses** | **[String]** | Human-readable statuses of the webhooks triggered during this turn. | [optional] 



## Enum: [FailureReasonsEnum]


* `FAILURE_REASON_UNSPECIFIED` (value: `"FAILURE_REASON_UNSPECIFIED"`)

* `FAILED_INTENT` (value: `"FAILED_INTENT"`)

* `FAILED_WEBHOOK` (value: `"FAILED_WEBHOOK"`)




