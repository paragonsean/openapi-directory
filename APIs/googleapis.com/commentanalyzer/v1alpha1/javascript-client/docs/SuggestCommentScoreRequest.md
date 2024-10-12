# PerspectiveCommentAnalyzerApi.SuggestCommentScoreRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributeScores** | [**{String: AttributeScores}**](AttributeScores.md) | Attribute scores for the comment. The map keys are attribute names, same as the requested_attribute field in AnalyzeCommentRequest (for example \&quot;ATTACK_ON_AUTHOR\&quot;, \&quot;INFLAMMATORY\&quot;, etc.). This field has the same type as the &#x60;attribute_scores&#x60; field in AnalyzeCommentResponse. To specify an overall attribute score for the entire comment as a whole, use the &#x60;summary_score&#x60; field of the mapped AttributeScores object. To specify scores on specific subparts of the comment, use the &#x60;span_scores&#x60; field. All SpanScore objects must have begin and end fields set. All Score objects must be explicitly set (for binary classification, use the score values 0 and 1). If Score objects don&#39;t include a ScoreType, &#x60;PROBABILITY&#x60; is assumed. &#x60;attribute_scores&#x60; must not be empty. The mapped AttributeScores objects also must not be empty. An &#x60;INVALID_ARGUMENT&#x60; error is returned for all malformed requests. | [optional] 
**clientToken** | **String** | Opaque token that is echoed from the request to the response. | [optional] 
**comment** | [**TextEntry**](TextEntry.md) |  | [optional] 
**communityId** | **String** | Optional identifier associating this comment score suggestion with a particular sub-community. Different communities may have different norms and rules. Specifying this value enables training community-specific models. | [optional] 
**context** | [**Context**](Context.md) |  | [optional] 
**languages** | **[String]** | The language(s) of the comment and context. If none are specified, we attempt to automatically detect the language. Both ISO and BCP-47 language codes are accepted. | [optional] 
**sessionId** | **String** | Session ID. Used to join related RPCs into a single session. For example, an interactive tool that calls both the AnalyzeComment and SuggestCommentScore RPCs should set all invocations of both RPCs to the same Session ID, typically a random 64-bit integer. | [optional] 


