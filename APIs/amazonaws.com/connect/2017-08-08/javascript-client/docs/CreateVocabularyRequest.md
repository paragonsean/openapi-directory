# AmazonConnectService.CreateVocabularyRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clientToken** | **String** | A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see &lt;a href&#x3D;\&quot;https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/\&quot;&gt;Making retries safe with idempotent APIs&lt;/a&gt;. If a create request is received more than once with same client token, subsequent requests return the previous response without creating a vocabulary again. | [optional] 
**vocabularyName** | **String** | A unique name of the custom vocabulary. | 
**languageCode** | **String** | The language code of the vocabulary entries. For a list of languages and their corresponding language codes, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/transcribe/latest/dg/transcribe-whatis.html\&quot;&gt;What is Amazon Transcribe?&lt;/a&gt;  | 
**content** | **String** | The content of the custom vocabulary in plain-text format with a table of values. Each row in the table represents a word or a phrase, described with &lt;code&gt;Phrase&lt;/code&gt;, &lt;code&gt;IPA&lt;/code&gt;, &lt;code&gt;SoundsLike&lt;/code&gt;, and &lt;code&gt;DisplayAs&lt;/code&gt; fields. Separate the fields with TAB characters. The size limit is 50KB. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/transcribe/latest/dg/custom-vocabulary.html#create-vocabulary-table\&quot;&gt;Create a custom vocabulary using a table&lt;/a&gt;. | 
**tags** | **{String: String}** | The tags used to organize, track, or control access for this resource. For example, { \&quot;tags\&quot;: {\&quot;key1\&quot;:\&quot;value1\&quot;, \&quot;key2\&quot;:\&quot;value2\&quot;} }. | [optional] 



## Enum: LanguageCodeEnum


* `ar-AE` (value: `"ar-AE"`)

* `de-CH` (value: `"de-CH"`)

* `de-DE` (value: `"de-DE"`)

* `en-AB` (value: `"en-AB"`)

* `en-AU` (value: `"en-AU"`)

* `en-GB` (value: `"en-GB"`)

* `en-IE` (value: `"en-IE"`)

* `en-IN` (value: `"en-IN"`)

* `en-US` (value: `"en-US"`)

* `en-WL` (value: `"en-WL"`)

* `es-ES` (value: `"es-ES"`)

* `es-US` (value: `"es-US"`)

* `fr-CA` (value: `"fr-CA"`)

* `fr-FR` (value: `"fr-FR"`)

* `hi-IN` (value: `"hi-IN"`)

* `it-IT` (value: `"it-IT"`)

* `ja-JP` (value: `"ja-JP"`)

* `ko-KR` (value: `"ko-KR"`)

* `pt-BR` (value: `"pt-BR"`)

* `pt-PT` (value: `"pt-PT"`)

* `zh-CN` (value: `"zh-CN"`)

* `en-NZ` (value: `"en-NZ"`)

* `en-ZA` (value: `"en-ZA"`)




