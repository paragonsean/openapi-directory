

# ListGiftCardsRequest

A request to list gift cards. You can optionally specify a filter to retrieve a subset of  gift cards.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cursor** | **String** | A pagination cursor returned by a previous call to this endpoint. Provide this cursor to retrieve the next set of results for the original query. If a cursor is not provided, it returns the first page of the results.  For more information, see [Pagination](https://developer.squareup.com/docs/docs/working-with-apis/pagination). |  [optional] |
|**customerId** | **String** | If a value is provided, returns only the gift cards linked to the specified customer |  [optional] |
|**limit** | **Integer** | If a value is provided, it returns only that number of results per page. The maximum number of results allowed per page is 50. The default value is 30. |  [optional] |
|**state** | **String** | If the state is provided, it returns the gift cards in the specified state  (see [GiftCardStatus](https://developer.squareup.com/reference/square_2021-08-18/enums/GiftCardStatus)). Otherwise, it returns the gift cards of all states. |  [optional] |
|**type** | **String** | If a type is provided, gift cards of this type are returned  (see [GiftCardType](https://developer.squareup.com/reference/square_2021-08-18/enums/GiftCardType)). If no type is provided, it returns gift cards of all types. |  [optional] |



