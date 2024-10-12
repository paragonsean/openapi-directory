# DialogflowApi.GoogleCloudDialogflowV2Intent

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **String** | Optional. The name of the action associated with the intent. Note: The action name must not contain whitespaces. | [optional] 
**defaultResponsePlatforms** | **[String]** | Optional. The list of platforms for which the first responses will be copied from the messages in PLATFORM_UNSPECIFIED (i.e. default platform). | [optional] 
**displayName** | **String** | Required. The name of this intent. | [optional] 
**endInteraction** | **Boolean** | Optional. Indicates that this intent ends an interaction. Some integrations (e.g., Actions on Google or Dialogflow phone gateway) use this information to close interaction with an end user. Default is false. | [optional] 
**events** | **[String]** | Optional. The collection of event names that trigger the intent. If the collection of input contexts is not empty, all of the contexts must be present in the active user session for an event to trigger this intent. Event names are limited to 150 characters. | [optional] 
**followupIntentInfo** | [**[GoogleCloudDialogflowV2IntentFollowupIntentInfo]**](GoogleCloudDialogflowV2IntentFollowupIntentInfo.md) | Output only. Read-only. Information about all followup intents that have this intent as a direct or indirect parent. We populate this field only in the output. | [optional] [readonly] 
**inputContextNames** | **[String]** | Optional. The list of context names required for this intent to be triggered. Format: &#x60;projects//agent/sessions/-/contexts/&#x60;. | [optional] 
**isFallback** | **Boolean** | Optional. Indicates whether this is a fallback intent. | [optional] 
**liveAgentHandoff** | **Boolean** | Optional. Indicates that a live agent should be brought in to handle the interaction with the user. In most cases, when you set this flag to true, you would also want to set end_interaction to true as well. Default is false. | [optional] 
**messages** | [**[GoogleCloudDialogflowV2IntentMessage]**](GoogleCloudDialogflowV2IntentMessage.md) | Optional. The collection of rich messages corresponding to the &#x60;Response&#x60; field in the Dialogflow console. | [optional] 
**mlDisabled** | **Boolean** | Optional. Indicates whether Machine Learning is disabled for the intent. Note: If &#x60;ml_disabled&#x60; setting is set to true, then this intent is not taken into account during inference in &#x60;ML ONLY&#x60; match mode. Also, auto-markup in the UI is turned off. | [optional] 
**name** | **String** | Optional. The unique identifier of this intent. Required for Intents.UpdateIntent and Intents.BatchUpdateIntents methods. Format: &#x60;projects//agent/intents/&#x60;. | [optional] 
**outputContexts** | [**[GoogleCloudDialogflowV2Context]**](GoogleCloudDialogflowV2Context.md) | Optional. The collection of contexts that are activated when the intent is matched. Context messages in this collection should not set the parameters field. Setting the &#x60;lifespan_count&#x60; to 0 will reset the context when the intent is matched. Format: &#x60;projects//agent/sessions/-/contexts/&#x60;. | [optional] 
**parameters** | [**[GoogleCloudDialogflowV2IntentParameter]**](GoogleCloudDialogflowV2IntentParameter.md) | Optional. The collection of parameters associated with the intent. | [optional] 
**parentFollowupIntentName** | **String** | Read-only after creation. The unique identifier of the parent intent in the chain of followup intents. You can set this field when creating an intent, for example with CreateIntent or BatchUpdateIntents, in order to make this intent a followup intent. It identifies the parent followup intent. Format: &#x60;projects//agent/intents/&#x60;. | [optional] 
**priority** | **Number** | Optional. The priority of this intent. Higher numbers represent higher priorities. - If the supplied value is unspecified or 0, the service translates the value to 500,000, which corresponds to the &#x60;Normal&#x60; priority in the console. - If the supplied value is negative, the intent is ignored in runtime detect intent requests. | [optional] 
**resetContexts** | **Boolean** | Optional. Indicates whether to delete all contexts in the current session when this intent is matched. | [optional] 
**rootFollowupIntentName** | **String** | Output only. Read-only. The unique identifier of the root intent in the chain of followup intents. It identifies the correct followup intents chain for this intent. We populate this field only in the output. Format: &#x60;projects//agent/intents/&#x60;. | [optional] [readonly] 
**trainingPhrases** | [**[GoogleCloudDialogflowV2IntentTrainingPhrase]**](GoogleCloudDialogflowV2IntentTrainingPhrase.md) | Optional. The collection of examples that the agent is trained on. | [optional] 
**webhookState** | **String** | Optional. Indicates whether webhooks are enabled for the intent. | [optional] 



## Enum: [DefaultResponsePlatformsEnum]


* `PLATFORM_UNSPECIFIED` (value: `"PLATFORM_UNSPECIFIED"`)

* `FACEBOOK` (value: `"FACEBOOK"`)

* `SLACK` (value: `"SLACK"`)

* `TELEGRAM` (value: `"TELEGRAM"`)

* `KIK` (value: `"KIK"`)

* `SKYPE` (value: `"SKYPE"`)

* `LINE` (value: `"LINE"`)

* `VIBER` (value: `"VIBER"`)

* `ACTIONS_ON_GOOGLE` (value: `"ACTIONS_ON_GOOGLE"`)

* `GOOGLE_HANGOUTS` (value: `"GOOGLE_HANGOUTS"`)





## Enum: WebhookStateEnum


* `UNSPECIFIED` (value: `"WEBHOOK_STATE_UNSPECIFIED"`)

* `ENABLED` (value: `"WEBHOOK_STATE_ENABLED"`)

* `ENABLED_FOR_SLOT_FILLING` (value: `"WEBHOOK_STATE_ENABLED_FOR_SLOT_FILLING"`)




