# AmazonCloudSearch.SynonymOptionsStatus

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**options** | **String** | Maps terms to their synonyms, serialized as a JSON document. The document has a single object with one property \&quot;synonyms\&quot; whose value is an object mapping terms to their synonyms. Each synonym is a simple string or an array of strings. The maximum size of a stopwords document is 100 KB. Example: &lt;code&gt;{ \&quot;synonyms\&quot;: {\&quot;cat\&quot;: [\&quot;feline\&quot;, \&quot;kitten\&quot;], \&quot;puppy\&quot;: \&quot;dog\&quot;} }&lt;/code&gt; | 
**status** | [**OptionStatus**](OptionStatus.md) |  | 


