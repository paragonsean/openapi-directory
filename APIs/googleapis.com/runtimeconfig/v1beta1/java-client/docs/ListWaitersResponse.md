

# ListWaitersResponse

Response for the `ListWaiters()` method. Order of returned waiter objects is arbitrary.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nextPageToken** | **String** | This token allows you to get the next page of results for list requests. If the number of results is larger than &#x60;pageSize&#x60;, use the &#x60;nextPageToken&#x60; as a value for the query parameter &#x60;pageToken&#x60; in the next list request. Subsequent list requests will have their own &#x60;nextPageToken&#x60; to continue paging through the results |  [optional] |
|**waiters** | [**List&lt;Waiter&gt;**](Waiter.md) | Found waiters in the project. |  [optional] |



