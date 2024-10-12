

# AnalyzeCommentResponse

The comment analysis response message.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attributeScores** | [**Map&lt;String, AttributeScores&gt;**](AttributeScores.md) | Scores for the requested attributes. The map keys are attribute names (same as the requested_attribute field in AnalyzeCommentRequest, for example \&quot;ATTACK_ON_AUTHOR\&quot;, \&quot;INFLAMMATORY\&quot;, etc). |  [optional] |
|**clientToken** | **String** | Same token from the original AnalyzeCommentRequest. |  [optional] |
|**detectedLanguages** | **List&lt;String&gt;** | Contains the languages detected from the text content, sorted in order of likelihood. |  [optional] |
|**languages** | **List&lt;String&gt;** | The language(s) used by CommentAnalyzer service to choose which Model to use when analyzing the comment. Might better be called \&quot;effective_languages\&quot;. The logic used to make the choice is as follows: if !Request.languages.empty() effective_languages &#x3D; Request.languages else effective_languages &#x3D; detected_languages[0] |  [optional] |



