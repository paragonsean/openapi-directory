

# LanguageLabsAidaTrustRecitationProtoStreamRecitationResult

The recitation result for one stream input

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dynamicSegmentResults** | [**List&lt;LanguageLabsAidaTrustRecitationProtoSegmentResult&gt;**](LanguageLabsAidaTrustRecitationProtoSegmentResult.md) | The recitation result against the given dynamic data source. |  [optional] |
|**fullyCheckedTextIndex** | **Integer** | Last index of input text fully checked for recitation in the entire streaming context. Would return &#x60;-1&#x60; if no Input was checked for recitation. |  [optional] |
|**recitationAction** | [**RecitationActionEnum**](#RecitationActionEnum) | The recitation action for one given input. When its segments contain different actions, the overall action will be returned in the precedence of BLOCK &gt; CITE &gt; NO_ACTION. |  [optional] |
|**trainingSegmentResults** | [**List&lt;LanguageLabsAidaTrustRecitationProtoSegmentResult&gt;**](LanguageLabsAidaTrustRecitationProtoSegmentResult.md) | The recitation result against model training data. |  [optional] |



## Enum: RecitationActionEnum

| Name | Value |
|---- | -----|
| ACTION_UNSPECIFIED | &quot;ACTION_UNSPECIFIED&quot; |
| CITE | &quot;CITE&quot; |
| BLOCK | &quot;BLOCK&quot; |
| NO_ACTION | &quot;NO_ACTION&quot; |
| EXEMPT_FOUND_IN_PROMPT | &quot;EXEMPT_FOUND_IN_PROMPT&quot; |



