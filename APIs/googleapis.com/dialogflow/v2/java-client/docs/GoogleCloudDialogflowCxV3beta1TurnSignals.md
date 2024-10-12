

# GoogleCloudDialogflowCxV3beta1TurnSignals

Collection of all signals that were extracted for a single turn of the conversation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**agentEscalated** | **Boolean** | Whether agent responded with LiveAgentHandoff fulfillment. |  [optional] |
|**dtmfUsed** | **Boolean** | Whether user was using DTMF input. |  [optional] |
|**failureReasons** | [**List&lt;FailureReasonsEnum&gt;**](#List&lt;FailureReasonsEnum&gt;) | Failure reasons of the turn. |  [optional] |
|**noMatch** | **Boolean** | Whether NLU predicted NO_MATCH. |  [optional] |
|**noUserInput** | **Boolean** | Whether user provided no input. |  [optional] |
|**reachedEndPage** | **Boolean** | Whether turn resulted in End Session page. |  [optional] |
|**sentimentMagnitude** | **Float** | Sentiment magnitude of the user utterance if [sentiment](https://cloud.google.com/dialogflow/cx/docs/concept/sentiment) was enabled. |  [optional] |
|**sentimentScore** | **Float** | Sentiment score of the user utterance if [sentiment](https://cloud.google.com/dialogflow/cx/docs/concept/sentiment) was enabled. |  [optional] |
|**userEscalated** | **Boolean** | Whether user was specifically asking for a live agent. |  [optional] |
|**webhookStatuses** | **List&lt;String&gt;** | Human-readable statuses of the webhooks triggered during this turn. |  [optional] |



## Enum: List&lt;FailureReasonsEnum&gt;

| Name | Value |
|---- | -----|
| FAILURE_REASON_UNSPECIFIED | &quot;FAILURE_REASON_UNSPECIFIED&quot; |
| FAILED_INTENT | &quot;FAILED_INTENT&quot; |
| FAILED_WEBHOOK | &quot;FAILED_WEBHOOK&quot; |



