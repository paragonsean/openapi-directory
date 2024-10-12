# DialogflowApi.GoogleCloudDialogflowV2ConversationProfile

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**automatedAgentConfig** | [**GoogleCloudDialogflowV2AutomatedAgentConfig**](GoogleCloudDialogflowV2AutomatedAgentConfig.md) |  | [optional] 
**createTime** | **String** | Output only. Create time of the conversation profile. | [optional] [readonly] 
**displayName** | **String** | Required. Human readable name for this profile. Max length 1024 bytes. | [optional] 
**humanAgentAssistantConfig** | [**GoogleCloudDialogflowV2HumanAgentAssistantConfig**](GoogleCloudDialogflowV2HumanAgentAssistantConfig.md) |  | [optional] 
**humanAgentHandoffConfig** | [**GoogleCloudDialogflowV2HumanAgentHandoffConfig**](GoogleCloudDialogflowV2HumanAgentHandoffConfig.md) |  | [optional] 
**languageCode** | **String** | Language code for the conversation profile. If not specified, the language is en-US. Language at ConversationProfile should be set for all non en-US languages. This should be a [BCP-47](https://www.rfc-editor.org/rfc/bcp/bcp47.txt) language tag. Example: \&quot;en-US\&quot;. | [optional] 
**loggingConfig** | [**GoogleCloudDialogflowV2LoggingConfig**](GoogleCloudDialogflowV2LoggingConfig.md) |  | [optional] 
**name** | **String** | The unique identifier of this conversation profile. Format: &#x60;projects//locations//conversationProfiles/&#x60;. | [optional] 
**newMessageEventNotificationConfig** | [**GoogleCloudDialogflowV2NotificationConfig**](GoogleCloudDialogflowV2NotificationConfig.md) |  | [optional] 
**notificationConfig** | [**GoogleCloudDialogflowV2NotificationConfig**](GoogleCloudDialogflowV2NotificationConfig.md) |  | [optional] 
**securitySettings** | **String** | Name of the CX SecuritySettings reference for the agent. Format: &#x60;projects//locations//securitySettings/&#x60;. | [optional] 
**sttConfig** | [**GoogleCloudDialogflowV2SpeechToTextConfig**](GoogleCloudDialogflowV2SpeechToTextConfig.md) |  | [optional] 
**timeZone** | **String** | The time zone of this conversational profile from the [time zone database](https://www.iana.org/time-zones), e.g., America/New_York, Europe/Paris. Defaults to America/New_York. | [optional] 
**ttsConfig** | [**GoogleCloudDialogflowV2SynthesizeSpeechConfig**](GoogleCloudDialogflowV2SynthesizeSpeechConfig.md) |  | [optional] 
**updateTime** | **String** | Output only. Update time of the conversation profile. | [optional] [readonly] 


