# PerspectiveCommentAnalyzerApi.SpanScore

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**begin** | **Number** | \&quot;begin\&quot; and \&quot;end\&quot; describe the span of the original text that the attribute score applies to. The values are the UTF-16 codepoint range. \&quot;end\&quot; is exclusive. For example, with the text \&quot;Hi there\&quot;, the begin/end pair (0,2) describes the text \&quot;Hi\&quot;. If \&quot;begin\&quot; and \&quot;end\&quot; are unset, the score applies to the full text. | [optional] 
**end** | **Number** |  | [optional] 
**score** | [**Score**](Score.md) |  | [optional] 


