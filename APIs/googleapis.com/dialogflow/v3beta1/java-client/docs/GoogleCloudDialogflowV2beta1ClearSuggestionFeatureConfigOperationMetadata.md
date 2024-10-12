

# GoogleCloudDialogflowV2beta1ClearSuggestionFeatureConfigOperationMetadata

Metadata for a ConversationProfile.ClearSuggestionFeatureConfig operation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**conversationProfile** | **String** | The resource name of the conversation profile. Format: &#x60;projects//locations//conversationProfiles/&#x60; |  [optional] |
|**createTime** | **String** | Timestamp whe the request was created. The time is measured on server side. |  [optional] |
|**participantRole** | [**ParticipantRoleEnum**](#ParticipantRoleEnum) | Required. The participant role to remove the suggestion feature config. Only HUMAN_AGENT or END_USER can be used. |  [optional] |
|**suggestionFeatureType** | [**SuggestionFeatureTypeEnum**](#SuggestionFeatureTypeEnum) | Required. The type of the suggestion feature to remove. |  [optional] |



## Enum: ParticipantRoleEnum

| Name | Value |
|---- | -----|
| ROLE_UNSPECIFIED | &quot;ROLE_UNSPECIFIED&quot; |
| HUMAN_AGENT | &quot;HUMAN_AGENT&quot; |
| AUTOMATED_AGENT | &quot;AUTOMATED_AGENT&quot; |
| END_USER | &quot;END_USER&quot; |



## Enum: SuggestionFeatureTypeEnum

| Name | Value |
|---- | -----|
| TYPE_UNSPECIFIED | &quot;TYPE_UNSPECIFIED&quot; |
| ARTICLE_SUGGESTION | &quot;ARTICLE_SUGGESTION&quot; |
| FAQ | &quot;FAQ&quot; |
| SMART_REPLY | &quot;SMART_REPLY&quot; |
| DIALOGFLOW_ASSIST | &quot;DIALOGFLOW_ASSIST&quot; |
| CONVERSATION_SUMMARIZATION | &quot;CONVERSATION_SUMMARIZATION&quot; |
| KNOWLEDGE_SEARCH | &quot;KNOWLEDGE_SEARCH&quot; |



