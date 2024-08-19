# AmazonLocationService.SearchPlaceIndexForPositionRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**language** | **String** | &lt;p&gt;The preferred language used to return results. The value must be a valid &lt;a href&#x3D;\&quot;https://tools.ietf.org/search/bcp47\&quot;&gt;BCP 47&lt;/a&gt; language tag, for example, &lt;code&gt;en&lt;/code&gt; for English.&lt;/p&gt; &lt;p&gt;This setting affects the languages used in the results, but not the results themselves. If no language is specified, or not supported for a particular result, the partner automatically chooses a language for the result.&lt;/p&gt; &lt;p&gt;For an example, we&#39;ll use the Greek language. You search for a location around Athens, Greece, with the &lt;code&gt;language&lt;/code&gt; parameter set to &lt;code&gt;en&lt;/code&gt;. The &lt;code&gt;city&lt;/code&gt; in the results will most likely be returned as &lt;code&gt;Athens&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;If you set the &lt;code&gt;language&lt;/code&gt; parameter to &lt;code&gt;el&lt;/code&gt;, for Greek, then the &lt;code&gt;city&lt;/code&gt; in the results will more likely be returned as &lt;code&gt;Αθήνα&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;If the data provider does not have a value for Greek, the result will be in a language that the provider does support.&lt;/p&gt; | [optional] 
**maxResults** | **Number** | &lt;p&gt;An optional parameter. The maximum number of results returned per request.&lt;/p&gt; &lt;p&gt;Default value: &lt;code&gt;50&lt;/code&gt; &lt;/p&gt; | [optional] 
**position** | **[Number]** | &lt;p&gt;Specifies the longitude and latitude of the position to query.&lt;/p&gt; &lt;p&gt; This parameter must contain a pair of numbers. The first number represents the X coordinate, or longitude; the second number represents the Y coordinate, or latitude.&lt;/p&gt; &lt;p&gt;For example, &lt;code&gt;[-123.1174, 49.2847]&lt;/code&gt; represents a position with longitude &lt;code&gt;-123.1174&lt;/code&gt; and latitude &lt;code&gt;49.2847&lt;/code&gt;.&lt;/p&gt; | 


