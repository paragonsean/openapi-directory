# VertexAiApi.LanguageLabsAidaTrustRecitationProtoStreamRecitationResult

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dynamicSegmentResults** | [**[LanguageLabsAidaTrustRecitationProtoSegmentResult]**](LanguageLabsAidaTrustRecitationProtoSegmentResult.md) | The recitation result against the given dynamic data source. | [optional] 
**fullyCheckedTextIndex** | **Number** | Last index of input text fully checked for recitation in the entire streaming context. Would return &#x60;-1&#x60; if no Input was checked for recitation. | [optional] 
**recitationAction** | **String** | The recitation action for one given input. When its segments contain different actions, the overall action will be returned in the precedence of BLOCK &gt; CITE &gt; NO_ACTION. | [optional] 
**trainingSegmentResults** | [**[LanguageLabsAidaTrustRecitationProtoSegmentResult]**](LanguageLabsAidaTrustRecitationProtoSegmentResult.md) | The recitation result against model training data. | [optional] 



## Enum: RecitationActionEnum


* `ACTION_UNSPECIFIED` (value: `"ACTION_UNSPECIFIED"`)

* `CITE` (value: `"CITE"`)

* `BLOCK` (value: `"BLOCK"`)

* `NO_ACTION` (value: `"NO_ACTION"`)

* `EXEMPT_FOUND_IN_PROMPT` (value: `"EXEMPT_FOUND_IN_PROMPT"`)




