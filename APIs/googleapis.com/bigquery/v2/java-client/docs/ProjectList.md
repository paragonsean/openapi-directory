

# ProjectList

Response object of ListProjects

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**etag** | **String** | A hash of the page of results. |  [optional] |
|**kind** | **String** | The resource type of the response. |  [optional] |
|**nextPageToken** | **String** | Use this token to request the next page of results. |  [optional] |
|**projects** | [**List&lt;ProjectListProjectsInner&gt;**](ProjectListProjectsInner.md) | Projects to which the user has at least READ access. |  [optional] |
|**totalItems** | **Integer** | The total number of projects in the page. A wrapper is used here because the field should still be in the response when the value is 0. |  [optional] |



