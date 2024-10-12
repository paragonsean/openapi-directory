# DialogflowApi.GoogleCloudDialogflowV2ClearSuggestionFeatureConfigRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**participantRole** | **String** | Required. The participant role to remove the suggestion feature config. Only HUMAN_AGENT or END_USER can be used. | [optional] 
**suggestionFeatureType** | **String** | Required. The type of the suggestion feature to remove. | [optional] 



## Enum: ParticipantRoleEnum


* `ROLE_UNSPECIFIED` (value: `"ROLE_UNSPECIFIED"`)

* `HUMAN_AGENT` (value: `"HUMAN_AGENT"`)

* `AUTOMATED_AGENT` (value: `"AUTOMATED_AGENT"`)

* `END_USER` (value: `"END_USER"`)





## Enum: SuggestionFeatureTypeEnum


* `TYPE_UNSPECIFIED` (value: `"TYPE_UNSPECIFIED"`)

* `ARTICLE_SUGGESTION` (value: `"ARTICLE_SUGGESTION"`)

* `FAQ` (value: `"FAQ"`)

* `SMART_REPLY` (value: `"SMART_REPLY"`)

* `KNOWLEDGE_SEARCH` (value: `"KNOWLEDGE_SEARCH"`)




