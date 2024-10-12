

# ListPaymentsResponse

Defines the response returned by [ListPayments](https://developer.squareup.com/reference/square_2021-08-18/payments-api/list-payments).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cursor** | **String** | The pagination cursor to be used in a subsequent request. If empty, this is the final response.  For more information, see [Pagination](https://developer.squareup.com/docs/basics/api101/pagination). |  [optional] |
|**errors** | [**List&lt;Error&gt;**](Error.md) | Information about errors encountered during the request. |  [optional] |
|**payments** | [**List&lt;Payment&gt;**](Payment.md) | The requested list of payments. |  [optional] |



