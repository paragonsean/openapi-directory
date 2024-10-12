# GmailApi.ListThreadsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nextPageToken** | **String** | Page token to retrieve the next page of results in the list. | [optional] 
**resultSizeEstimate** | **Number** | Estimated total number of results. | [optional] 
**threads** | [**[Thread]**](Thread.md) | List of threads. Note that each thread resource does not contain a list of &#x60;messages&#x60;. The list of &#x60;messages&#x60; for a given thread can be fetched using the threads.get method. | [optional] 


