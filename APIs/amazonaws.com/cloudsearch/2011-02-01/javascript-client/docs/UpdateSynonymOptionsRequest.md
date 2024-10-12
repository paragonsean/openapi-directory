# AmazonCloudSearch.UpdateSynonymOptionsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domainName** | **String** | A string that represents the name of a domain. Domain names must be unique across the domains owned by an account within an AWS region. Domain names must start with a letter or number and can contain the following characters: a-z (lowercase), 0-9, and - (hyphen). Uppercase letters and underscores are not allowed. | 
**synonyms** | **String** | Maps terms to their synonyms, serialized as a JSON document. The document has a single object with one property \&quot;synonyms\&quot; whose value is an object mapping terms to their synonyms. Each synonym is a simple string or an array of strings. The maximum size of a stopwords document is 100 KB. Example: &lt;code&gt;{ \&quot;synonyms\&quot;: {\&quot;cat\&quot;: [\&quot;feline\&quot;, \&quot;kitten\&quot;], \&quot;puppy\&quot;: \&quot;dog\&quot;} }&lt;/code&gt; | 


