

# ListPaymentRefundsResponse

Defines the response returned by [ListPaymentRefunds](https://developer.squareup.com/reference/square_2021-08-18/refunds-api/list-payment-refunds).  Either `errors` or `refunds` is present in a given response (never both).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cursor** | **String** | The pagination cursor to be used in a subsequent request. If empty, this is the final response.  For more information, see [Pagination](https://developer.squareup.com/docs/basics/api101/pagination). |  [optional] |
|**errors** | [**List&lt;Error&gt;**](Error.md) | Information about errors encountered during the request. |  [optional] |
|**refunds** | [**List&lt;PaymentRefund&gt;**](PaymentRefund.md) | The list of requested refunds. |  [optional] |



