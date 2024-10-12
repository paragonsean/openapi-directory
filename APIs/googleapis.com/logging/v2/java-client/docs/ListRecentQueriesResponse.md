

# ListRecentQueriesResponse

The response from ListRecentQueries.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nextPageToken** | **String** | If there might be more results than appear in this response, then nextPageToken is included. To get the next set of results, call the same method again using the value of nextPageToken as pageToken. |  [optional] |
|**recentQueries** | [**List&lt;RecentQuery&gt;**](RecentQuery.md) | A list of recent queries. |  [optional] |
|**unreachable** | **List&lt;String&gt;** | The unreachable resources. Each resource can be either 1) a saved query if a specific query is unreachable or 2) a location if a specific location is unreachable. \&quot;projects/[PROJECT_ID]/locations/[LOCATION_ID]/recentQueries/[QUERY_ID]\&quot; \&quot;projects/[PROJECT_ID]/locations/[LOCATION_ID]\&quot; For example:\&quot;projects/my-project/locations/global/recentQueries/12345678\&quot; \&quot;projects/my-project/locations/global\&quot;If there are unreachable resources, the response will first return pages that contain recent queries, and then return pages that contain the unreachable resources. |  [optional] |



