

# GETDefineExpressionExpressionParameter

A named expression that can be evaluated at search time. Can be used to sort the search results, define other expressions, or return computed information in the search results. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**expressionName** | **String** | Names must begin with a letter and can contain the following characters: a-z (lowercase), 0-9, and _ (underscore). |  |
|**expressionValue** | **String** | The expression to evaluate for sorting while processing a search request. The &lt;code&gt;Expression&lt;/code&gt; syntax is based on JavaScript expressions. For more information, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-expressions.html\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Configuring Expressions&lt;/a&gt; in the &lt;i&gt;Amazon CloudSearch Developer Guide&lt;/i&gt;. |  |



