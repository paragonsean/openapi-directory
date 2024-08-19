# VertexAiApi.LearningGenaiRecitationRecitationResult

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dynamicSegmentResults** | [**[LearningGenaiRecitationSegmentResult]**](LearningGenaiRecitationSegmentResult.md) |  | [optional] 
**recitationAction** | **String** | The recitation action for one given input. When its segments contain different actions, the overall action will be returned in the precedence of BLOCK &gt; CITE &gt; NO_ACTION. When the given input is not found in any source, the recitation action will be NO_ACTION. | [optional] 
**trainingSegmentResults** | [**[LearningGenaiRecitationSegmentResult]**](LearningGenaiRecitationSegmentResult.md) |  | [optional] 



## Enum: RecitationActionEnum


* `ACTION_UNSPECIFIED` (value: `"ACTION_UNSPECIFIED"`)

* `CITE` (value: `"CITE"`)

* `BLOCK` (value: `"BLOCK"`)

* `NO_ACTION` (value: `"NO_ACTION"`)

* `EXEMPT_FOUND_IN_PROMPT` (value: `"EXEMPT_FOUND_IN_PROMPT"`)




