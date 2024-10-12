

# NlpSaftLangIdLocalesResult


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**predictions** | [**List&lt;NlpSaftLangIdLocalesResultLocale&gt;**](NlpSaftLangIdLocalesResultLocale.md) | List of locales in which the text would be considered acceptable. Sorted in descending order according to each locale&#39;s respective likelihood. For example, if a Portuguese text is acceptable in both Brazil and Portugal, but is more strongly associated with Brazil, then the predictions would be [\&quot;pt-BR\&quot;, \&quot;pt-PT\&quot;], in that order. May be empty, indicating that the model did not predict any acceptable locales. |  [optional] |



