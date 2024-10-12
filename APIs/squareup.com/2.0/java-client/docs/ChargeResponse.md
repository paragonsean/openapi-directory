

# ChargeResponse

Defines the fields that are included in the response body of a request to the [Charge](https://developer.squareup.com/reference/square_2021-08-18/transactions-api/charge) endpoint.  One of `errors` or `transaction` is present in a given response (never both).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**errors** | [**List&lt;Error&gt;**](Error.md) | Any errors that occurred during the request. |  [optional] |
|**transaction** | [**Transaction**](Transaction.md) |  |  [optional] |



