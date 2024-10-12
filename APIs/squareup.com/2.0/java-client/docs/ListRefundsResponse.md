

# ListRefundsResponse

Defines the fields that are included in the response body of a request to the [ListRefunds](https://developer.squareup.com/reference/square_2021-08-18/transactions-api/list-refunds) endpoint.  One of `errors` or `refunds` is present in a given response (never both).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cursor** | **String** | A pagination cursor for retrieving the next set of results, if any remain. Provide this value as the &#x60;cursor&#x60; parameter in a subsequent request to this endpoint.  See [Paginating results](https://developer.squareup.com/docs/working-with-apis/pagination) for more information. |  [optional] |
|**errors** | [**List&lt;Error&gt;**](Error.md) | Any errors that occurred during the request. |  [optional] |
|**refunds** | [**List&lt;Refund&gt;**](Refund.md) | An array of refunds that match your query. |  [optional] |



