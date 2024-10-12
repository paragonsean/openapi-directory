# AmazonLexModelBuildingV2.ListUtteranceMetricsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**startDateTime** | **Date** | The date and time that marks the beginning of the range of time for which you want to see utterance metrics. | 
**endDateTime** | **Date** | The date and time that marks the end of the range of time for which you want to see utterance metrics. | 
**metrics** | [**[AnalyticsUtteranceMetric]**](AnalyticsUtteranceMetric.md) | A list of objects, each of which contains a metric you want to list, the statistic for the metric you want to return, and the method by which to organize the results. | 
**binBy** | [**[AnalyticsBinBySpecification]**](AnalyticsBinBySpecification.md) | A list of objects, each of which contains specifications for organizing the results by time. | [optional] 
**groupBy** | [**[AnalyticsUtteranceGroupBySpecification]**](AnalyticsUtteranceGroupBySpecification.md) | &lt;p&gt;A list of objects, each of which specifies how to group the results. You can group by the following criteria:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;UtteranceText&lt;/code&gt; – The transcription of the utterance.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;UtteranceState&lt;/code&gt; – The state of the utterance. The possible states are detailed in &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/analytics-key-definitions-utterances\&quot;&gt;Key definitions&lt;/a&gt; in the user guide.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; | [optional] 
**attributes** | [**[AnalyticsUtteranceAttribute]**](AnalyticsUtteranceAttribute.md) | &lt;p&gt;A list containing attributes related to the utterance that you want the response to return. The following attributes are possible:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;LastUsedIntent&lt;/code&gt; – The last used intent at the time of the utterance.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; | [optional] 
**filters** | [**[AnalyticsUtteranceFilter]**](AnalyticsUtteranceFilter.md) | A list of objects, each of which describes a condition by which you want to filter the results. | [optional] 
**maxResults** | **Number** | The maximum number of results to return in each page of results. If there are fewer results than the maximum page size, only the actual number of results are returned. | [optional] 
**nextToken** | **String** | &lt;p&gt;If the response from the ListUtteranceMetrics operation contains more results than specified in the maxResults parameter, a token is returned in the response.&lt;/p&gt; &lt;p&gt;Use the returned token in the nextToken parameter of a ListUtteranceMetrics request to return the next page of results. For a complete set of results, call the ListUtteranceMetrics operation until the nextToken returned in the response is null.&lt;/p&gt; | [optional] 


