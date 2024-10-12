# ContactCenterAiInsightsApi.GoogleCloudContactcenterinsightsV1alpha1Conversation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agentId** | **String** | An opaque, user-specified string representing the human agent who handled the conversation. | [optional] 
**callMetadata** | [**GoogleCloudContactcenterinsightsV1alpha1ConversationCallMetadata**](GoogleCloudContactcenterinsightsV1alpha1ConversationCallMetadata.md) |  | [optional] 
**createTime** | **String** | Output only. The time at which the conversation was created. | [optional] [readonly] 
**dataSource** | [**GoogleCloudContactcenterinsightsV1alpha1ConversationDataSource**](GoogleCloudContactcenterinsightsV1alpha1ConversationDataSource.md) |  | [optional] 
**dialogflowIntents** | [**{String: GoogleCloudContactcenterinsightsV1alpha1DialogflowIntent}**](GoogleCloudContactcenterinsightsV1alpha1DialogflowIntent.md) | Output only. All the matched Dialogflow intents in the call. The key corresponds to a Dialogflow intent, format: projects/{project}/agent/{agent}/intents/{intent} | [optional] [readonly] 
**duration** | **String** | Output only. The duration of the conversation. | [optional] [readonly] 
**expireTime** | **String** | The time at which this conversation should expire. After this time, the conversation data and any associated analyses will be deleted. | [optional] 
**labels** | **{String: String}** | A map for the user to specify any custom fields. A maximum of 20 labels per conversation is allowed, with a maximum of 256 characters per entry. | [optional] 
**languageCode** | **String** | A user-specified language code for the conversation. | [optional] 
**latestAnalysis** | [**GoogleCloudContactcenterinsightsV1alpha1Analysis**](GoogleCloudContactcenterinsightsV1alpha1Analysis.md) |  | [optional] 
**latestSummary** | [**GoogleCloudContactcenterinsightsV1alpha1ConversationSummarizationSuggestionData**](GoogleCloudContactcenterinsightsV1alpha1ConversationSummarizationSuggestionData.md) |  | [optional] 
**medium** | **String** | Immutable. The conversation medium, if unspecified will default to PHONE_CALL. | [optional] 
**name** | **String** | Immutable. The resource name of the conversation. Format: projects/{project}/locations/{location}/conversations/{conversation} | [optional] 
**obfuscatedUserId** | **String** | Obfuscated user ID which the customer sent to us. | [optional] 
**qualityMetadata** | [**GoogleCloudContactcenterinsightsV1alpha1ConversationQualityMetadata**](GoogleCloudContactcenterinsightsV1alpha1ConversationQualityMetadata.md) |  | [optional] 
**runtimeAnnotations** | [**[GoogleCloudContactcenterinsightsV1alpha1RuntimeAnnotation]**](GoogleCloudContactcenterinsightsV1alpha1RuntimeAnnotation.md) | Output only. The annotations that were generated during the customer and agent interaction. | [optional] [readonly] 
**startTime** | **String** | The time at which the conversation started. | [optional] 
**transcript** | [**GoogleCloudContactcenterinsightsV1alpha1ConversationTranscript**](GoogleCloudContactcenterinsightsV1alpha1ConversationTranscript.md) |  | [optional] 
**ttl** | **String** | Input only. The TTL for this resource. If specified, then this TTL will be used to calculate the expire time. | [optional] 
**turnCount** | **Number** | Output only. The number of turns in the conversation. | [optional] [readonly] 
**updateTime** | **String** | Output only. The most recent time at which the conversation was updated. | [optional] [readonly] 



## Enum: MediumEnum


* `MEDIUM_UNSPECIFIED` (value: `"MEDIUM_UNSPECIFIED"`)

* `PHONE_CALL` (value: `"PHONE_CALL"`)

* `CHAT` (value: `"CHAT"`)




