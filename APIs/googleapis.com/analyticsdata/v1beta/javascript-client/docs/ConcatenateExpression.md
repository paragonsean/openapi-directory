# GoogleAnalyticsDataApi.ConcatenateExpression

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delimiter** | **String** | The delimiter placed between dimension names. Delimiters are often single characters such as \&quot;|\&quot; or \&quot;,\&quot; but can be longer strings. If a dimension value contains the delimiter, both will be present in response with no distinction. For example if dimension 1 value &#x3D; \&quot;US,FR\&quot;, dimension 2 value &#x3D; \&quot;JP\&quot;, and delimiter &#x3D; \&quot;,\&quot;, then the response will contain \&quot;US,FR,JP\&quot;. | [optional] 
**dimensionNames** | **[String]** | Names of dimensions. The names must refer back to names in the dimensions field of the request. | [optional] 


