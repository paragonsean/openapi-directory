

# ListCardsResponse

Defines the fields that are included in the response body of a request to the [ListCards](#endpoint-cards-listcards) endpoint.  Note: if there are errors processing the request, the card field will not be present.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cards** | [**List&lt;Card&gt;**](Card.md) | The requested list of &#x60;Card&#x60;s. |  [optional] |
|**cursor** | **String** | The pagination cursor to be used in a subsequent request. If empty, this is the final response.  See [Pagination](https://developer.squareup.com/docs/basics/api101/pagination) for more information. |  [optional] |
|**errors** | [**List&lt;Error&gt;**](Error.md) | Information on errors encountered during the request. |  [optional] |



