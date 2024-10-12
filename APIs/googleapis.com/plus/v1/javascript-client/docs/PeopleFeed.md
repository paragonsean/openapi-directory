# GoogleApi.PeopleFeed

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**etag** | **String** | ETag of this response for caching purposes. | [optional] 
**items** | [**[Person]**](Person.md) | The people in this page of results. Each item includes the id, displayName, image, and url for the person. To retrieve additional profile data, see the people.get method. | [optional] 
**kind** | **String** | Identifies this resource as a collection of people. Value: \&quot;plus#peopleFeed\&quot;. | [optional] [default to &#39;plus#peopleFeed&#39;]
**nextPageToken** | **String** | The continuation token, which is used to page through large result sets. Provide this value in a subsequent request to return the next page of results. | [optional] 
**selfLink** | **String** | Link to this resource. | [optional] 
**title** | **String** | The title of this collection of people. | [optional] 
**totalItems** | **Number** | The total number of people available in this list. The number of people in a response might be smaller due to paging. This might not be set for all collections. | [optional] 


