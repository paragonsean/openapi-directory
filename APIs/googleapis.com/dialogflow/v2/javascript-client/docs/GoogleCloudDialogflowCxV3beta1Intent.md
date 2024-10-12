# DialogflowApi.GoogleCloudDialogflowCxV3beta1Intent

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **String** | Human readable description for better understanding an intent like its scope, content, result etc. Maximum character limit: 140 characters. | [optional] 
**displayName** | **String** | Required. The human-readable name of the intent, unique within the agent. | [optional] 
**isFallback** | **Boolean** | Indicates whether this is a fallback intent. Currently only default fallback intent is allowed in the agent, which is added upon agent creation. Adding training phrases to fallback intent is useful in the case of requests that are mistakenly matched, since training phrases assigned to fallback intents act as negative examples that triggers no-match event. | [optional] 
**labels** | **{String: String}** | The key/value metadata to label an intent. Labels can contain lowercase letters, digits and the symbols &#39;-&#39; and &#39;_&#39;. International characters are allowed, including letters from unicase alphabets. Keys must start with a letter. Keys and values can be no longer than 63 characters and no more than 128 bytes. Prefix \&quot;sys-\&quot; is reserved for Dialogflow defined labels. Currently allowed Dialogflow defined labels include: * sys-head * sys-contextual The above labels do not require value. \&quot;sys-head\&quot; means the intent is a head intent. \&quot;sys-contextual\&quot; means the intent is a contextual intent. | [optional] 
**name** | **String** | The unique identifier of the intent. Required for the Intents.UpdateIntent method. Intents.CreateIntent populates the name automatically. Format: &#x60;projects//locations//agents//intents/&#x60;. | [optional] 
**parameters** | [**[GoogleCloudDialogflowCxV3beta1IntentParameter]**](GoogleCloudDialogflowCxV3beta1IntentParameter.md) | The collection of parameters associated with the intent. | [optional] 
**priority** | **Number** | The priority of this intent. Higher numbers represent higher priorities. - If the supplied value is unspecified or 0, the service translates the value to 500,000, which corresponds to the &#x60;Normal&#x60; priority in the console. - If the supplied value is negative, the intent is ignored in runtime detect intent requests. | [optional] 
**trainingPhrases** | [**[GoogleCloudDialogflowCxV3beta1IntentTrainingPhrase]**](GoogleCloudDialogflowCxV3beta1IntentTrainingPhrase.md) | The collection of training phrases the agent is trained on to identify the intent. | [optional] 


