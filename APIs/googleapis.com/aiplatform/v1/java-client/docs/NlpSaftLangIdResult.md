

# NlpSaftLangIdResult


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**modelVersion** | [**ModelVersionEnum**](#ModelVersionEnum) | The version of the model used to create these annotations. |  [optional] |
|**predictions** | [**List&lt;NlpSaftLanguageSpan&gt;**](NlpSaftLanguageSpan.md) | This field stores the n-best list of possible BCP 47 language code strings for a given input sorted in descending order according to each code&#39;s respective probability. |  [optional] |
|**spanPredictions** | [**List&lt;NlpSaftLanguageSpanSequence&gt;**](NlpSaftLanguageSpanSequence.md) | This field stores language predictions of subspans of the input, when available. Each LanguageSpanSequence is a sequence of LanguageSpans. A particular sequence of LanguageSpans has an associated probability, and need not necessarily cover the entire input. If no language could be predicted for any span, then this field may be empty. |  [optional] |



## Enum: ModelVersionEnum

| Name | Value |
|---- | -----|
| VERSION_UNSPECIFIED | &quot;VERSION_UNSPECIFIED&quot; |
| INDEXING_20181017 | &quot;INDEXING_20181017&quot; |
| INDEXING_20191206 | &quot;INDEXING_20191206&quot; |
| INDEXING_20200313 | &quot;INDEXING_20200313&quot; |
| INDEXING_20210618 | &quot;INDEXING_20210618&quot; |
| STANDARD_20220516 | &quot;STANDARD_20220516&quot; |



