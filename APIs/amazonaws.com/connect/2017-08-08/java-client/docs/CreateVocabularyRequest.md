

# CreateVocabularyRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clientToken** | **String** | A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see &lt;a href&#x3D;\&quot;https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/\&quot;&gt;Making retries safe with idempotent APIs&lt;/a&gt;. If a create request is received more than once with same client token, subsequent requests return the previous response without creating a vocabulary again. |  [optional] |
|**vocabularyName** | **String** | A unique name of the custom vocabulary. |  |
|**languageCode** | [**LanguageCodeEnum**](#LanguageCodeEnum) | The language code of the vocabulary entries. For a list of languages and their corresponding language codes, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/transcribe/latest/dg/transcribe-whatis.html\&quot;&gt;What is Amazon Transcribe?&lt;/a&gt;  |  |
|**content** | **String** | The content of the custom vocabulary in plain-text format with a table of values. Each row in the table represents a word or a phrase, described with &lt;code&gt;Phrase&lt;/code&gt;, &lt;code&gt;IPA&lt;/code&gt;, &lt;code&gt;SoundsLike&lt;/code&gt;, and &lt;code&gt;DisplayAs&lt;/code&gt; fields. Separate the fields with TAB characters. The size limit is 50KB. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/transcribe/latest/dg/custom-vocabulary.html#create-vocabulary-table\&quot;&gt;Create a custom vocabulary using a table&lt;/a&gt;. |  |
|**tags** | **Map&lt;String, String&gt;** | The tags used to organize, track, or control access for this resource. For example, { \&quot;tags\&quot;: {\&quot;key1\&quot;:\&quot;value1\&quot;, \&quot;key2\&quot;:\&quot;value2\&quot;} }. |  [optional] |



## Enum: LanguageCodeEnum

| Name | Value |
|---- | -----|
| AR_AE | &quot;ar-AE&quot; |
| DE_CH | &quot;de-CH&quot; |
| DE_DE | &quot;de-DE&quot; |
| EN_AB | &quot;en-AB&quot; |
| EN_AU | &quot;en-AU&quot; |
| EN_GB | &quot;en-GB&quot; |
| EN_IE | &quot;en-IE&quot; |
| EN_IN | &quot;en-IN&quot; |
| EN_US | &quot;en-US&quot; |
| EN_WL | &quot;en-WL&quot; |
| ES_ES | &quot;es-ES&quot; |
| ES_US | &quot;es-US&quot; |
| FR_CA | &quot;fr-CA&quot; |
| FR_FR | &quot;fr-FR&quot; |
| HI_IN | &quot;hi-IN&quot; |
| IT_IT | &quot;it-IT&quot; |
| JA_JP | &quot;ja-JP&quot; |
| KO_KR | &quot;ko-KR&quot; |
| PT_BR | &quot;pt-BR&quot; |
| PT_PT | &quot;pt-PT&quot; |
| ZH_CN | &quot;zh-CN&quot; |
| EN_NZ | &quot;en-NZ&quot; |
| EN_ZA | &quot;en-ZA&quot; |



