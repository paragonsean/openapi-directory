

# SearchLoyaltyEventsResponse

A response that contains loyalty events that satisfy the search  criteria, in order by the `created_at` date.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cursor** | **String** | The pagination cursor to be used in a subsequent  request. If empty, this is the final response.  For more information,  see [Pagination](https://developer.squareup.com/docs/basics/api101/pagination). |  [optional] |
|**errors** | [**List&lt;Error&gt;**](Error.md) | Any errors that occurred during the request. |  [optional] |
|**events** | [**List&lt;LoyaltyEvent&gt;**](LoyaltyEvent.md) | The loyalty events that satisfy the search criteria. |  [optional] |



