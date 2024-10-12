# DialogflowApi.GoogleCloudDialogflowCxV3Agent

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advancedSettings** | [**GoogleCloudDialogflowCxV3AdvancedSettings**](GoogleCloudDialogflowCxV3AdvancedSettings.md) |  | [optional] 
**answerFeedbackSettings** | [**GoogleCloudDialogflowCxV3AgentAnswerFeedbackSettings**](GoogleCloudDialogflowCxV3AgentAnswerFeedbackSettings.md) |  | [optional] 
**avatarUri** | **String** | The URI of the agent&#39;s avatar. Avatars are used throughout the Dialogflow console and in the self-hosted [Web Demo](https://cloud.google.com/dialogflow/docs/integrations/web-demo) integration. | [optional] 
**defaultLanguageCode** | **String** | Required. Immutable. The default language of the agent as a language tag. See [Language Support](https://cloud.google.com/dialogflow/cx/docs/reference/language) for a list of the currently supported language codes. This field cannot be set by the Agents.UpdateAgent method. | [optional] 
**description** | **String** | The description of the agent. The maximum length is 500 characters. If exceeded, the request is rejected. | [optional] 
**displayName** | **String** | Required. The human-readable name of the agent, unique within the location. | [optional] 
**enableSpellCorrection** | **Boolean** | Indicates if automatic spell correction is enabled in detect intent requests. | [optional] 
**enableStackdriverLogging** | **Boolean** | Indicates if stackdriver logging is enabled for the agent. Please use agent.advanced_settings instead. | [optional] 
**genAppBuilderSettings** | [**GoogleCloudDialogflowCxV3AgentGenAppBuilderSettings**](GoogleCloudDialogflowCxV3AgentGenAppBuilderSettings.md) |  | [optional] 
**gitIntegrationSettings** | [**GoogleCloudDialogflowCxV3AgentGitIntegrationSettings**](GoogleCloudDialogflowCxV3AgentGitIntegrationSettings.md) |  | [optional] 
**locked** | **Boolean** | Indicates whether the agent is locked for changes. If the agent is locked, modifications to the agent will be rejected except for RestoreAgent. | [optional] 
**name** | **String** | The unique identifier of the agent. Required for the Agents.UpdateAgent method. Agents.CreateAgent populates the name automatically. Format: &#x60;projects//locations//agents/&#x60;. | [optional] 
**securitySettings** | **String** | Name of the SecuritySettings reference for the agent. Format: &#x60;projects//locations//securitySettings/&#x60;. | [optional] 
**speechToTextSettings** | [**GoogleCloudDialogflowCxV3SpeechToTextSettings**](GoogleCloudDialogflowCxV3SpeechToTextSettings.md) |  | [optional] 
**startFlow** | **String** | Immutable. Name of the start flow in this agent. A start flow will be automatically created when the agent is created, and can only be deleted by deleting the agent. Format: &#x60;projects//locations//agents//flows/&#x60;. | [optional] 
**supportedLanguageCodes** | **[String]** | The list of all languages supported by the agent (except for the &#x60;default_language_code&#x60;). | [optional] 
**textToSpeechSettings** | [**GoogleCloudDialogflowCxV3TextToSpeechSettings**](GoogleCloudDialogflowCxV3TextToSpeechSettings.md) |  | [optional] 
**timeZone** | **String** | Required. The time zone of the agent from the [time zone database](https://www.iana.org/time-zones), e.g., America/New_York, Europe/Paris. | [optional] 


