

# ListRefundsRequest

Defines the query parameters that can be included in a request to the [ListRefunds](https://developer.squareup.com/reference/square_2021-08-18/transactions-api/list-refunds) endpoint.  Deprecated - recommend using [SearchOrders](https://developer.squareup.com/reference/square_2021-08-18/orders-api/search-orders)

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**beginTime** | **String** | The beginning of the requested reporting period, in RFC 3339 format.  See [Date ranges](https://developer.squareup.com/docs/build-basics/working-with-dates) for details on date inclusivity/exclusivity.  Default value: The current time minus one year. |  [optional] |
|**cursor** | **String** | A pagination cursor returned by a previous call to this endpoint. Provide this to retrieve the next set of results for your original query.  See [Paginating results](https://developer.squareup.com/docs/working-with-apis/pagination) for more information. |  [optional] |
|**endTime** | **String** | The end of the requested reporting period, in RFC 3339 format.  See [Date ranges](https://developer.squareup.com/docs/build-basics/working-with-dates) for details on date inclusivity/exclusivity.  Default value: The current time. |  [optional] |
|**sortOrder** | **String** | The order in which results are listed in the response (&#x60;ASC&#x60; for oldest first, &#x60;DESC&#x60; for newest first).  Default value: &#x60;DESC&#x60; |  [optional] |



