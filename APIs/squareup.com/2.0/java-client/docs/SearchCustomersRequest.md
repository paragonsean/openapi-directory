

# SearchCustomersRequest

Defines the fields that are included in the request body of a request to the `SearchCustomers` endpoint.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cursor** | **String** | Include the pagination cursor in subsequent calls to this endpoint to retrieve the next set of results associated with the original query.  For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination). |  [optional] |
|**limit** | **Long** | The maximum number of results to return in a single page. This limit is advisory. The response might contain more or fewer results.  The limit is ignored if it is less than the minimum or greater than the maximum value. The default value is 100.  For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination). |  [optional] |
|**query** | [**CustomerQuery**](CustomerQuery.md) |  |  [optional] |



