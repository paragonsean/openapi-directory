

# ListSessionAnalyticsDataRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**startDateTime** | **OffsetDateTime** | The date and time that marks the beginning of the range of time for which you want to see session analytics. |  |
|**endDateTime** | **OffsetDateTime** | The date and time that marks the end of the range of time for which you want to see session analytics. |  |
|**sortBy** | [**ListSessionAnalyticsDataRequestSortBy**](ListSessionAnalyticsDataRequestSortBy.md) |  |  [optional] |
|**filters** | [**List&lt;AnalyticsSessionFilter&gt;**](AnalyticsSessionFilter.md) | A list of objects, each of which describes a condition by which you want to filter the results. |  [optional] |
|**maxResults** | **Integer** | The maximum number of results to return in each page of results. If there are fewer results than the maximum page size, only the actual number of results are returned. |  [optional] |
|**nextToken** | **String** | &lt;p&gt;If the response from the ListSessionAnalyticsData operation contains more results than specified in the maxResults parameter, a token is returned in the response.&lt;/p&gt; &lt;p&gt;Use the returned token in the nextToken parameter of a ListSessionAnalyticsData request to return the next page of results. For a complete set of results, call the ListSessionAnalyticsData operation until the nextToken returned in the response is null.&lt;/p&gt; |  [optional] |



