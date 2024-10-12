

# SearchCustomersResponse

Defines the fields that are included in the response body of a request to the `SearchCustomers` endpoint.  Either `errors` or `customers` is present in a given response (never both).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cursor** | **String** | A pagination cursor that can be used during subsequent calls to &#x60;SearchCustomers&#x60; to retrieve the next set of results associated with the original query. Pagination cursors are only present when a request succeeds and additional results are available.  For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination). |  [optional] |
|**customers** | [**List&lt;Customer&gt;**](Customer.md) | An array of &#x60;Customer&#x60; objects that match a query. |  [optional] |
|**errors** | [**List&lt;Error&gt;**](Error.md) | Any errors that occurred during the request. |  [optional] |



