# GoogleApi.ActivityFeed

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**etag** | **String** | ETag of this response for caching purposes. | [optional] 
**id** | **String** | The ID of this collection of activities. Deprecated. | [optional] 
**items** | [**[Activity]**](Activity.md) | The activities in this page of results. | [optional] 
**kind** | **String** | Identifies this resource as a collection of activities. Value: \&quot;plus#activityFeed\&quot;. | [optional] [default to &#39;plus#activityFeed&#39;]
**nextLink** | **String** | Link to the next page of activities. | [optional] 
**nextPageToken** | **String** | The continuation token, which is used to page through large result sets. Provide this value in a subsequent request to return the next page of results. | [optional] 
**selfLink** | **String** | Link to this activity resource. | [optional] 
**title** | **String** | The title of this collection of activities, which is a truncated portion of the content. | [optional] 
**updated** | **Date** | The time at which this collection of activities was last updated. Formatted as an RFC 3339 timestamp. | [optional] 


