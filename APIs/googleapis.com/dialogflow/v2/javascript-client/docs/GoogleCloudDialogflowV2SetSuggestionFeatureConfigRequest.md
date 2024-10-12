# DialogflowApi.GoogleCloudDialogflowV2SetSuggestionFeatureConfigRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**participantRole** | **String** | Required. The participant role to add or update the suggestion feature config. Only HUMAN_AGENT or END_USER can be used. | [optional] 
**suggestionFeatureConfig** | [**GoogleCloudDialogflowV2HumanAgentAssistantConfigSuggestionFeatureConfig**](GoogleCloudDialogflowV2HumanAgentAssistantConfigSuggestionFeatureConfig.md) |  | [optional] 



## Enum: ParticipantRoleEnum


* `ROLE_UNSPECIFIED` (value: `"ROLE_UNSPECIFIED"`)

* `HUMAN_AGENT` (value: `"HUMAN_AGENT"`)

* `AUTOMATED_AGENT` (value: `"AUTOMATED_AGENT"`)

* `END_USER` (value: `"END_USER"`)




