

# ListIntentStageMetricsRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**startDateTime** | **OffsetDateTime** | The date and time that marks the beginning of the range of time for which you want to see intent stage metrics. |  |
|**endDateTime** | **OffsetDateTime** | The date and time that marks the end of the range of time for which you want to see intent stage metrics. |  |
|**metrics** | [**List&lt;AnalyticsIntentStageMetric&gt;**](AnalyticsIntentStageMetric.md) | A list of objects, each of which contains a metric you want to list, the statistic for the metric you want to return, and the method by which to organize the results. |  |
|**binBy** | [**List&lt;AnalyticsBinBySpecification&gt;**](AnalyticsBinBySpecification.md) | A list of objects, each of which contains specifications for organizing the results by time. |  [optional] |
|**groupBy** | [**List&lt;AnalyticsIntentStageGroupBySpecification&gt;**](AnalyticsIntentStageGroupBySpecification.md) | &lt;p&gt;A list of objects, each of which specifies how to group the results. You can group by the following criteria:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;IntentStageName&lt;/code&gt; – The name of the intent stage.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;SwitchedToIntent&lt;/code&gt; – The intent to which the conversation was switched (if any).&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; |  [optional] |
|**filters** | [**List&lt;AnalyticsIntentStageFilter&gt;**](AnalyticsIntentStageFilter.md) | A list of objects, each of which describes a condition by which you want to filter the results. |  [optional] |
|**maxResults** | **Integer** | The maximum number of results to return in each page of results. If there are fewer results than the maximum page size, only the actual number of results are returned. |  [optional] |
|**nextToken** | **String** | &lt;p&gt;If the response from the ListIntentStageMetrics operation contains more results than specified in the maxResults parameter, a token is returned in the response.&lt;/p&gt; &lt;p&gt;Use the returned token in the nextToken parameter of a ListIntentStageMetrics request to return the next page of results. For a complete set of results, call the ListIntentStageMetrics operation until the nextToken returned in the response is null.&lt;/p&gt; |  [optional] |



