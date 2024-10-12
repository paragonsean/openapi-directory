

# ListSavedQueriesResponse

The response from ListSavedQueries.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nextPageToken** | **String** | If there might be more results than appear in this response, then nextPageToken is included. To get the next set of results, call the same method again using the value of nextPageToken as pageToken. |  [optional] |
|**savedQueries** | [**List&lt;SavedQuery&gt;**](SavedQuery.md) | A list of saved queries. |  [optional] |
|**unreachable** | **List&lt;String&gt;** | The unreachable resources. It can be either 1) a saved query if a specific query is unreachable or 2) a location if a specific location is unreachabe. \&quot;projects/[PROJECT_ID]/locations/[LOCATION_ID]/savedQueries/[QUERY_ID]\&quot; \&quot;projects/[PROJECT_ID]/locations/[LOCATION_ID]\&quot; For example: \&quot;projects/my-project/locations/global/savedQueries/12345678\&quot; \&quot;projects/my-project/locations/global\&quot; If there are unreachable resources, the response will first return pages that contain saved queries, and then return pages that contain the unreachable resources. |  [optional] |



