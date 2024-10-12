

# ListThreadsResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nextPageToken** | **String** | Page token to retrieve the next page of results in the list. |  [optional] |
|**resultSizeEstimate** | **Integer** | Estimated total number of results. |  [optional] |
|**threads** | [**List&lt;Thread&gt;**](Thread.md) | List of threads. Note that each thread resource does not contain a list of &#x60;messages&#x60;. The list of &#x60;messages&#x60; for a given thread can be fetched using the threads.get method. |  [optional] |



