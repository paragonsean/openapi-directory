

# SearchLoyaltyEventsRequest

A request to search for loyalty events.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cursor** | **String** | A pagination cursor returned by a previous call to this endpoint. Provide this to retrieve the next set of results for your original query. For more information, see [Pagination](https://developer.squareup.com/docs/basics/api101/pagination). |  [optional] |
|**limit** | **Integer** | The maximum number of results to include in the response.  The last page might contain fewer events.  The default is 30 events. |  [optional] |
|**query** | [**LoyaltyEventQuery**](LoyaltyEventQuery.md) |  |  [optional] |



