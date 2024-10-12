# AmazonLexModelBuildingV2.ListSessionMetricsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**startDateTime** | **Date** | The date and time that marks the beginning of the range of time for which you want to see session metrics. | 
**endDateTime** | **Date** | The date and time that marks the end of the range of time for which you want to see session metrics. | 
**metrics** | [**[AnalyticsSessionMetric]**](AnalyticsSessionMetric.md) | A list of objects, each of which contains a metric you want to list, the statistic for the metric you want to return, and the method by which to organize the results. | 
**binBy** | [**[AnalyticsBinBySpecification]**](AnalyticsBinBySpecification.md) | A list of objects, each of which contains specifications for organizing the results by time. | [optional] 
**groupBy** | [**[AnalyticsSessionGroupBySpecification]**](AnalyticsSessionGroupBySpecification.md) | &lt;p&gt;A list of objects, each of which specifies how to group the results. You can group by the following criteria:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ConversationEndState&lt;/code&gt; – The final state of the conversation. The possible end states are detailed in &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/analytics-key-definitions-conversations\&quot;&gt;Key definitions&lt;/a&gt; in the user guide.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;LocaleId&lt;/code&gt; – The unique identifier of the bot locale.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; | [optional] 
**filters** | [**[AnalyticsSessionFilter]**](AnalyticsSessionFilter.md) | A list of objects, each of which describes a condition by which you want to filter the results. | [optional] 
**maxResults** | **Number** | The maximum number of results to return in each page of results. If there are fewer results than the maximum page size, only the actual number of results are returned. | [optional] 
**nextToken** | **String** | &lt;p&gt;If the response from the ListSessionMetrics operation contains more results than specified in the maxResults parameter, a token is returned in the response.&lt;/p&gt; &lt;p&gt;Use the returned token in the nextToken parameter of a ListSessionMetrics request to return the next page of results. For a complete set of results, call the ListSessionMetrics operation until the nextToken returned in the response is null.&lt;/p&gt; | [optional] 


