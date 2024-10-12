

# UpdateStopwordOptionsRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**domainName** | **String** | A string that represents the name of a domain. Domain names must be unique across the domains owned by an account within an AWS region. Domain names must start with a letter or number and can contain the following characters: a-z (lowercase), 0-9, and - (hyphen). Uppercase letters and underscores are not allowed. |  |
|**stopwords** | **String** | Lists stopwords serialized as a JSON document. The document has a single object with one property \&quot;stopwords\&quot; whose value is an array of strings. The maximum size of a stopwords document is 10 KB. Example: &lt;code&gt;{ \&quot;stopwords\&quot;: [\&quot;a\&quot;, \&quot;an\&quot;, \&quot;the\&quot;, \&quot;of\&quot;] }&lt;/code&gt; |  |



