

# GoogleCloudDialogflowV2beta1ConversationProfile

Defines the services to connect to incoming Dialogflow conversations.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**automatedAgentConfig** | [**GoogleCloudDialogflowV2beta1AutomatedAgentConfig**](GoogleCloudDialogflowV2beta1AutomatedAgentConfig.md) |  |  [optional] |
|**createTime** | **String** | Output only. Create time of the conversation profile. |  [optional] [readonly] |
|**displayName** | **String** | Required. Human readable name for this profile. Max length 1024 bytes. |  [optional] |
|**humanAgentAssistantConfig** | [**GoogleCloudDialogflowV2beta1HumanAgentAssistantConfig**](GoogleCloudDialogflowV2beta1HumanAgentAssistantConfig.md) |  |  [optional] |
|**humanAgentHandoffConfig** | [**GoogleCloudDialogflowV2beta1HumanAgentHandoffConfig**](GoogleCloudDialogflowV2beta1HumanAgentHandoffConfig.md) |  |  [optional] |
|**languageCode** | **String** | Language code for the conversation profile. If not specified, the language is en-US. Language at ConversationProfile should be set for all non en-us languages. This should be a [BCP-47](https://www.rfc-editor.org/rfc/bcp/bcp47.txt) language tag. Example: \&quot;en-US\&quot;. |  [optional] |
|**loggingConfig** | [**GoogleCloudDialogflowV2beta1LoggingConfig**](GoogleCloudDialogflowV2beta1LoggingConfig.md) |  |  [optional] |
|**name** | **String** | The unique identifier of this conversation profile. Format: &#x60;projects//locations//conversationProfiles/&#x60;. |  [optional] |
|**newMessageEventNotificationConfig** | [**GoogleCloudDialogflowV2beta1NotificationConfig**](GoogleCloudDialogflowV2beta1NotificationConfig.md) |  |  [optional] |
|**notificationConfig** | [**GoogleCloudDialogflowV2beta1NotificationConfig**](GoogleCloudDialogflowV2beta1NotificationConfig.md) |  |  [optional] |
|**securitySettings** | **String** | Name of the CX SecuritySettings reference for the agent. Format: &#x60;projects//locations//securitySettings/&#x60;. |  [optional] |
|**sttConfig** | [**GoogleCloudDialogflowV2beta1SpeechToTextConfig**](GoogleCloudDialogflowV2beta1SpeechToTextConfig.md) |  |  [optional] |
|**timeZone** | **String** | The time zone of this conversational profile from the [time zone database](https://www.iana.org/time-zones), e.g., America/New_York, Europe/Paris. Defaults to America/New_York. |  [optional] |
|**ttsConfig** | [**GoogleCloudDialogflowV2beta1SynthesizeSpeechConfig**](GoogleCloudDialogflowV2beta1SynthesizeSpeechConfig.md) |  |  [optional] |
|**updateTime** | **String** | Output only. Update time of the conversation profile. |  [optional] [readonly] |



