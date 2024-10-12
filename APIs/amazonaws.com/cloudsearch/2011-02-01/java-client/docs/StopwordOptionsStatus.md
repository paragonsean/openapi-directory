

# StopwordOptionsStatus

The stopword options configured for this search domain and the current status of those options.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**options** | **String** | Lists stopwords serialized as a JSON document. The document has a single object with one property \&quot;stopwords\&quot; whose value is an array of strings. The maximum size of a stopwords document is 10 KB. Example: &lt;code&gt;{ \&quot;stopwords\&quot;: [\&quot;a\&quot;, \&quot;an\&quot;, \&quot;the\&quot;, \&quot;of\&quot;] }&lt;/code&gt; |  |
|**status** | [**OptionStatus**](OptionStatus.md) |  |  |



