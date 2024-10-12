

# ListCustomerGroupsResponse

Defines the fields that are included in the response body of a request to the [ListCustomerGroups](https://developer.squareup.com/reference/square_2021-08-18/customer-groups-api/list-customer-groups) endpoint.  Either `errors` or `groups` is present in a given response (never both).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cursor** | **String** | A pagination cursor to retrieve the next set of results for your original query to the endpoint. This value is present only if the request succeeded and additional results are available.  For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination). |  [optional] |
|**errors** | [**List&lt;Error&gt;**](Error.md) | Any errors that occurred during the request. |  [optional] |
|**groups** | [**List&lt;CustomerGroup&gt;**](CustomerGroup.md) | A list of customer groups belonging to the current seller. |  [optional] |



