

# CloudAiNlLlmProtoServiceRaiResult

The RAI results for a given text.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**aidaRecitationResult** | [**LanguageLabsAidaTrustRecitationProtoRecitationResult**](LanguageLabsAidaTrustRecitationProtoRecitationResult.md) |  |  [optional] |
|**blocked** | **Boolean** | Use &#x60;triggered_blocklist&#x60;. |  [optional] |
|**errorCodes** | **List&lt;Integer&gt;** | The error codes indicate which RAI filters block the response. |  [optional] |
|**filtered** | **Boolean** | Whether the text should be filtered and not shown to the end user. This is determined based on a combination of &#x60;triggered_recitation&#x60;, &#x60;triggered_blocklist&#x60;, &#x60;language_filter_result&#x60;, and &#x60;triggered_safety_filter&#x60;. |  [optional] |
|**languageFilterResult** | [**LearningGenaiRootLanguageFilterResult**](LearningGenaiRootLanguageFilterResult.md) |  |  [optional] |
|**raiSignals** | [**List&lt;CloudAiNlLlmProtoServiceRaiSignal&gt;**](CloudAiNlLlmProtoServiceRaiSignal.md) | The RAI signals for the text. |  [optional] |
|**triggeredBlocklist** | **Boolean** | Whether the text triggered the blocklist. |  [optional] |
|**triggeredRecitation** | **Boolean** | Whether the text should be blocked by the recitation result from Aida recitation checker. It is determined from aida_recitation_result. |  [optional] |
|**triggeredSafetyFilter** | **Boolean** | Whether the text triggered the safety filter. Currently, this is due to CSAI triggering or one of four categories (derogatory, sexual, toxic, violent) having a score over the filter threshold. |  [optional] |



