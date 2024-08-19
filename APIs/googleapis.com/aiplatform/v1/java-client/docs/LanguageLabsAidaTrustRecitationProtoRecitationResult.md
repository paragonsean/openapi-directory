

# LanguageLabsAidaTrustRecitationProtoRecitationResult

The recitation result for one input

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dynamicSegmentResults** | [**List&lt;LanguageLabsAidaTrustRecitationProtoSegmentResult&gt;**](LanguageLabsAidaTrustRecitationProtoSegmentResult.md) |  |  [optional] |
|**recitationAction** | [**RecitationActionEnum**](#RecitationActionEnum) | The recitation action for one given input. When its segments contain different actions, the overall action will be returned in the precedence of BLOCK &gt; CITE &gt; NO_ACTION. When the given input is not found in any source, the recitation action will not be specified. |  [optional] |
|**trainingSegmentResults** | [**List&lt;LanguageLabsAidaTrustRecitationProtoSegmentResult&gt;**](LanguageLabsAidaTrustRecitationProtoSegmentResult.md) |  |  [optional] |



## Enum: RecitationActionEnum

| Name | Value |
|---- | -----|
| ACTION_UNSPECIFIED | &quot;ACTION_UNSPECIFIED&quot; |
| CITE | &quot;CITE&quot; |
| BLOCK | &quot;BLOCK&quot; |
| NO_ACTION | &quot;NO_ACTION&quot; |
| EXEMPT_FOUND_IN_PROMPT | &quot;EXEMPT_FOUND_IN_PROMPT&quot; |



