# VertexAiApi.NlpSaftLangIdResult

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**modelVersion** | **String** | The version of the model used to create these annotations. | [optional] 
**predictions** | [**[NlpSaftLanguageSpan]**](NlpSaftLanguageSpan.md) | This field stores the n-best list of possible BCP 47 language code strings for a given input sorted in descending order according to each code&#39;s respective probability. | [optional] 
**spanPredictions** | [**[NlpSaftLanguageSpanSequence]**](NlpSaftLanguageSpanSequence.md) | This field stores language predictions of subspans of the input, when available. Each LanguageSpanSequence is a sequence of LanguageSpans. A particular sequence of LanguageSpans has an associated probability, and need not necessarily cover the entire input. If no language could be predicted for any span, then this field may be empty. | [optional] 



## Enum: ModelVersionEnum


* `VERSION_UNSPECIFIED` (value: `"VERSION_UNSPECIFIED"`)

* `INDEXING_20181017` (value: `"INDEXING_20181017"`)

* `INDEXING_20191206` (value: `"INDEXING_20191206"`)

* `INDEXING_20200313` (value: `"INDEXING_20200313"`)

* `INDEXING_20210618` (value: `"INDEXING_20210618"`)

* `STANDARD_20220516` (value: `"STANDARD_20220516"`)




