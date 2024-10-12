# AmazonCloudSearch.StemmingOptionsStatus

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**options** | **String** | Maps terms to their stems, serialized as a JSON document. The document has a single object with one property \&quot;stems\&quot; whose value is an object mapping terms to their stems. The maximum size of a stemming document is 500 KB. Example: &lt;code&gt;{ \&quot;stems\&quot;: {\&quot;people\&quot;: \&quot;person\&quot;, \&quot;walking\&quot;: \&quot;walk\&quot;} }&lt;/code&gt; | 
**status** | [**OptionStatus**](OptionStatus.md) |  | 


