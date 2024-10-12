

# GoogleCloudDialogflowV2beta1KnowledgeAnswersAnswer

An answer from Knowledge Connector.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**answer** | **String** | The piece of text from the &#x60;source&#x60; knowledge base document that answers this conversational query. |  [optional] |
|**faqQuestion** | **String** | The corresponding FAQ question if the answer was extracted from a FAQ Document, empty otherwise. |  [optional] |
|**matchConfidence** | **Float** | The system&#39;s confidence score that this Knowledge answer is a good match for this conversational query. The range is from 0.0 (completely uncertain) to 1.0 (completely certain). Note: The confidence score is likely to vary somewhat (possibly even for identical requests), as the underlying model is under constant improvement. It may be deprecated in the future. We recommend using &#x60;match_confidence_level&#x60; which should be generally more stable. |  [optional] |
|**matchConfidenceLevel** | [**MatchConfidenceLevelEnum**](#MatchConfidenceLevelEnum) | The system&#39;s confidence level that this knowledge answer is a good match for this conversational query. NOTE: The confidence level for a given &#x60;&#x60; pair may change without notice, as it depends on models that are constantly being improved. However, it will change less frequently than the confidence score below, and should be preferred for referencing the quality of an answer. |  [optional] |
|**source** | **String** | Indicates which Knowledge Document this answer was extracted from. Format: &#x60;projects//knowledgeBases//documents/&#x60;. |  [optional] |



## Enum: MatchConfidenceLevelEnum

| Name | Value |
|---- | -----|
| MATCH_CONFIDENCE_LEVEL_UNSPECIFIED | &quot;MATCH_CONFIDENCE_LEVEL_UNSPECIFIED&quot; |
| LOW | &quot;LOW&quot; |
| MEDIUM | &quot;MEDIUM&quot; |
| HIGH | &quot;HIGH&quot; |



