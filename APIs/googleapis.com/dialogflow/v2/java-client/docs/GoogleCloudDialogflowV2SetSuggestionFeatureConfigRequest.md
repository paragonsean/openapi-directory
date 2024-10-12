

# GoogleCloudDialogflowV2SetSuggestionFeatureConfigRequest

The request message for ConversationProfiles.SetSuggestionFeature.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**participantRole** | [**ParticipantRoleEnum**](#ParticipantRoleEnum) | Required. The participant role to add or update the suggestion feature config. Only HUMAN_AGENT or END_USER can be used. |  [optional] |
|**suggestionFeatureConfig** | [**GoogleCloudDialogflowV2HumanAgentAssistantConfigSuggestionFeatureConfig**](GoogleCloudDialogflowV2HumanAgentAssistantConfigSuggestionFeatureConfig.md) |  |  [optional] |



## Enum: ParticipantRoleEnum

| Name | Value |
|---- | -----|
| ROLE_UNSPECIFIED | &quot;ROLE_UNSPECIFIED&quot; |
| HUMAN_AGENT | &quot;HUMAN_AGENT&quot; |
| AUTOMATED_AGENT | &quot;AUTOMATED_AGENT&quot; |
| END_USER | &quot;END_USER&quot; |



