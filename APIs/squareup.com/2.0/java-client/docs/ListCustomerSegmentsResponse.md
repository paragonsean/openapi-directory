

# ListCustomerSegmentsResponse

Defines the fields that are included in the response body for requests to the `ListCustomerSegments` endpoint.  Either `errors` or `segments` is present in a given response (never both).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cursor** | **String** | A pagination cursor to be used in subsequent calls to &#x60;ListCustomerSegments&#x60; to retrieve the next set of query results. The cursor is only present if the request succeeded and additional results are available.  For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination). |  [optional] |
|**errors** | [**List&lt;Error&gt;**](Error.md) | Any errors that occurred during the request. |  [optional] |
|**segments** | [**List&lt;CustomerSegment&gt;**](CustomerSegment.md) | The list of customer segments belonging to the associated Square account. |  [optional] |



