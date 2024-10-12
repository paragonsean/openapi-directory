

# ListIntentPathsRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**startDateTime** | **OffsetDateTime** | The date and time that marks the beginning of the range of time for which you want to see intent path metrics. |  |
|**endDateTime** | **OffsetDateTime** | The date and time that marks the end of the range of time for which you want to see intent path metrics. |  |
|**intentPath** | **String** | &lt;p&gt;The intent path for which you want to retrieve metrics. Use a forward slash to separate intents in the path. For example:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;/BookCar&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;/BookCar/BookHotel&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;/BookHotel/BookCar&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; |  |
|**filters** | [**List&lt;AnalyticsPathFilter&gt;**](AnalyticsPathFilter.md) | A list of objects, each describes a condition by which you want to filter the results. |  [optional] |



